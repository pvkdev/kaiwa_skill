"""Compiled navigation changes without editing chapter source or search rows."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_fork.py"
spec = importlib.util.spec_from_file_location("build_fork", SCRIPT)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class BuildNavigationTest(unittest.TestCase):
    def test_rewrites_only_in_scope_chapter_destinations(self) -> None:
        chapters = {"chapters/01-a.md", "chapters/sub/02-b.md"}
        source = (
            "[next](sub/02-b.md#u-b) [self](./01-a.md#u-a \"label\")\n"
            "[angle](<sub/02-b.md#u-b>) [missing](03-c.md#u-c)\n"
            "[web](https://example.org/02-b.md#u-b) [mail](mailto:a@example.org)\n"
            "[pdf](../source.pdf#page=2) [local](#u-a) ![image](sub/02-b.md#u-b)\n"
            "`[example](sub/02-b.md#u-b)` and ``[other](sub/02-b.md#u-b)``\n"
            "```md\n[code](sub/02-b.md#u-b)\n```\n"
            "~~~\n[fenced](sub/02-b.md#u-b)\n~~~\n"
            "  ```md\n  [indented code](sub/02-b.md#u-b)\n  ```  \n"
            "[after fence](sub/02-b.md#u-b)\n"
        )
        result = build.compiled_links(source, "chapters/01-a.md", chapters)
        self.assertIn("[next](#u-b)", result)
        self.assertIn('[self](#u-a "label")', result)
        self.assertIn("[angle](<#u-b>)", result)
        self.assertIn("[after fence](#u-b)", result)
        for unchanged in (
            "[missing](03-c.md#u-c)", "[web](https://example.org/02-b.md#u-b)",
            "[mail](mailto:a@example.org)", "[pdf](../source.pdf#page=2)",
            "[local](#u-a)", "![image](sub/02-b.md#u-b)",
            "`[example](sub/02-b.md#u-b)`", "``[other](sub/02-b.md#u-b)``",
            "[code](sub/02-b.md#u-b)", "[fenced](sub/02-b.md#u-b)",
            "  [indented code](sub/02-b.md#u-b)",
        ):
            self.assertIn(unchanged, result)
        self.assertEqual(result.count("#u-b"), source.count("#u-b"))

    def test_assemble_resolves_from_each_chapter_and_preserves_sources(self) -> None:
        with tempfile.TemporaryDirectory(prefix="build-navigation-") as temporary:
            book = Path(temporary)
            (book / "chapters/sub").mkdir(parents=True)
            (book / "_meta").mkdir()
            chapters = ["chapters/01-a.md", "chapters/sub/02-b.md"]
            first = '<a id="u-a"></a>\n# First\n[Go B](sub/02-b.md#u-b)\n'
            second = '<a id="u-b"></a>\n# Second\n[Go A](../01-a.md#u-a)\n'
            for relative, text in zip(chapters, (first, second)):
                (book / relative).write_text(text, encoding="utf-8")
            (book / "_meta/book.json").write_text(json.dumps({
                "title": "Sample", "status": "full", "scope": {"chapters": chapters},
            }), encoding="utf-8")
            (book / "_meta/units.jsonl").write_text("".join(json.dumps({
                "unit_id": unit_id, "chapter": chapter, "heading": unit_id, "source": [],
            }) + "\n" for unit_id, chapter in zip(("u-a", "u-b"), chapters)), encoding="utf-8")
            before = {relative: hashlib.sha256((book / relative).read_bytes()).hexdigest()
                      for relative in chapters}

            build.assemble(book)

            compiled = (book / "book.md").read_text(encoding="utf-8")
            search = (book / "_meta/search.jsonl").read_text(encoding="utf-8")
            self.assertIn("[Go B](#u-b)", compiled)
            self.assertIn("[Go A](#u-a)", compiled)
            self.assertNotIn("sub/02-b.md#u-b", compiled)
            self.assertNotIn("../01-a.md#u-a", compiled)
            self.assertIn("[Go B](sub/02-b.md#u-b)", search)
            self.assertIn("[Go A](../01-a.md#u-a)", search)
            self.assertEqual(before, {relative: hashlib.sha256((book / relative).read_bytes()).hexdigest()
                                      for relative in chapters})


if __name__ == "__main__":
    unittest.main()
