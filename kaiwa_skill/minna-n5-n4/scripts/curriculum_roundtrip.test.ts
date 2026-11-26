import { describe, expect, it } from "../../../../harumi/frontend/node_modules/vitest/dist/index.js";
import { readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import { buildExerciseCopyPayload, parseCopiedExerciseJson } from "../../../../harumi/frontend/src/lib/learning/curriculumExerciseCopyPaste";
import { sectionAdminKind } from "../../../../harumi/frontend/src/lib/learning/learningContentModel";
import { sectionsFromLessonExerciseContent, serializeSectionContent } from "../../../../harumi/frontend/src/lib/learning/learningContentMappers";

const dir = join(__dirname, "../exports/curriculum-exercises/lesson-39");
const index = JSON.parse(readFileSync(join(dir, "index.json"), "utf8"));

for (const [n, family] of [[39,"assessment"], [1,"listening"], [39,"listening"]] as const) {
  const lessonDir = "lesson-"+String(n).padStart(2,"0");
  const exportDir = join(__dirname, "../exports/curriculum-exercises", family, lessonDir);
  it(lessonDir+" "+family+" preserves authored answers, explanations and media", () => {
    const authored = JSON.parse(readFileSync(join(__dirname,"../authored",lessonDir,family+".json"),"utf8"));
    for (const section of authored.sections) {
      const native = JSON.parse(readFileSync(join(exportDir, section.id+".storage.json"), "utf8"));
      const [first] = sectionsFromLessonExerciseContent(native.format, JSON.stringify(native.content));
      const [loaded] = sectionsFromLessonExerciseContent(native.format, serializeSectionContent(first));
      expect(sectionAdminKind(loaded)).toBe(section.kind);
      expect(loaded.questions).toHaveLength(section.questions.length);
      for (const [i, question] of loaded.questions.entries()) {
        const expected = section.questions[i];
        expect(question.explanation).toBe(expected.explanation_vi);
        expect(question.choices.find((c) => c.id === question.correctChoiceId)?.text)
          .toBe(expected.choices.find((c) => c.id === expected.correct_choice_id).text);
      }
      if (family === "listening") {
        expect(loaded.jlptBlock.mediaItems[0].audio.scriptJaMd).toBe(section.media.script_ja);
        expect(loaded.jlptBlock.mediaItems[0].audio.url).toBe(section.media.url);
      }
    }
  });
}

describe("lesson 39 optional source readings", () => {
  const src = JSON.parse(readFileSync(join(__dirname, "../authored/lesson-39/reading.json"), "utf8"));
  const folder = join(__dirname, "../exports/curriculum-exercises/reading/lesson-39");
  for (const section of src.sections) {
    it(section.id, () => {
      const copy = readFileSync(join(folder, section.id + ".paste.json"), "utf8");
      const parsed = parseCopiedExerciseJson(copy);
      const [loaded] = sectionsFromLessonExerciseContent("Reading", serializeSectionContent(parsed));
      expect(sectionAdminKind(loaded)).toBe("jlptReading");
      expect(loaded.jlptBlock.mediaItems[0].passage.jaMd).toBe(section.media.ja);
      expect(loaded.questions).toHaveLength(section.questions.length);
      for (const [i, question] of loaded.questions.entries()) {
        const expected = section.questions[i];
        expect(question.explanation).toBe(expected.explanation_vi);
        expect(question.choices.find((c) => c.id === question.correctChoiceId)?.text)
          .toBe(expected.choices.find((c) => c.id === expected.correct_choice_id).text);
      }
    });
  }
});

describe("Minna native template copy, save and learner reload", () => {
  for (const row of index.sections) {
    it(`${row.kind}: native storage -> learner`, () => {
      const storage = JSON.parse(readFileSync(join(dir, row.storage_file), "utf8"));
      const [loaded] = sectionsFromLessonExerciseContent(storage.format, JSON.stringify(storage.content));
      expect(sectionAdminKind(loaded)).toBe(row.kind);
      expect(loaded.questions).toHaveLength(row.question_count);
      expect(loaded.questions.every((q) => typeof q.explanation === "string" && q.explanation.length > 0)).toBe(true);
      if (row.kind === "manualMultiSelect") expect(loaded.questions[0].correctChoiceIds).toEqual(["a", "c"]);
      if (row.kind === "manualFillInBlank") expect(loaded.questions.map((q) => q.blankAnswers?.[0]?.text)).toEqual(["途中で", "なので"]);
      if (row.kind === "jlptListening") {
        expect(loaded.jlptBlock?.mediaItems[0]?.audio?.scriptJaMd).toBe("地震のニュースを見て、びっくりしました。");
        expect(loaded.jlptBlock?.mediaItems[0]?.audio?.url).toContain("b1.mp3");
        const pasted = parseCopiedExerciseJson(JSON.stringify(buildExerciseCopyPayload(loaded)));
        const [reloaded] = sectionsFromLessonExerciseContent("Listening", serializeSectionContent(pasted));
        expect(reloaded.jlptBlock?.mediaItems[0]?.audio?.url).toBe(loaded.jlptBlock?.mediaItems[0]?.audio?.url);
        expect(reloaded.jlptBlock?.mediaItems[0]?.audio?.scriptJaMd).toBe(loaded.jlptBlock?.mediaItems[0]?.audio?.scriptJaMd);
      }
    });
    if (row.paste_file) {
      it(`${row.kind}: editor paste -> save -> learner`, () => {
        const payload = JSON.parse(readFileSync(join(dir, row.paste_file), "utf8"));
        const pasted = parseCopiedExerciseJson(JSON.stringify(payload));
        expect(sectionAdminKind(pasted)).toBe(row.kind);
        const [loaded] = sectionsFromLessonExerciseContent(payload.templateFormat, serializeSectionContent(pasted));
        expect(sectionAdminKind(loaded)).toBe(row.kind);
        expect(loaded.questions.map((q) => q.explanation)).toEqual(pasted.questions.map((q) => q.explanation));
        if (row.kind === "manualFillInBlank") expect(loaded.questions.map((q) => q.blankAnswers?.[0]?.text)).toEqual(["途中で", "なので"]);
      });
    }
  }
});

describe("50 lesson Renshuu adapter", () => {
  const base = join(__dirname, "../exports/curriculum-exercises/renshuu");
  for (const lessonDir of readdirSync(base).filter((x) => /^lesson-\d\d$/.test(x))) {
    it(lessonDir, () => {
      const authored = JSON.parse(readFileSync(join(__dirname, "../authored/renshuu", `${lessonDir}.json`), "utf8"));
      const idx = JSON.parse(readFileSync(join(base, lessonDir, "index.json"), "utf8"));
      expect(idx.sections).toHaveLength(authored.items.length);
      for (let i = 0; i < idx.sections.length; i++) {
        const row = idx.sections[i];
        const item = authored.items[i];
        const storage = JSON.parse(readFileSync(join(base, lessonDir, row.storage_file), "utf8"));
        const [loaded] = sectionsFromLessonExerciseContent(storage.format, JSON.stringify(storage.content));
        expect(sectionAdminKind(loaded)).toBe(item.kind);
        expect(loaded.questions[0].explanation).toBe(item.explanation_vi);
        if (item.kind === "manualQnA") {
          const correctText = item.choices.find((c: { id: string; text: string }) => c.id === item.correct)?.text;
          expect(loaded.questions[0].choices.find((c) => c.id === loaded.questions[0].correctChoiceId)?.text).toBe(correctText);
          expect(row.paste_file).toBeNull();
        } else {
          expect(loaded.questions[0].blankAnswers?.[0]?.text).toBe(item.correct);
          expect(row.paste_file).toBeTruthy();
        }
      }
    });
  }
});

describe("50 lesson grammar quick checks", () => {
  const base = join(__dirname, "../exports/curriculum-exercises/quick-checks");
  for (const lessonDir of readdirSync(base).filter((x) => /^lesson-\d\d$/.test(x))) {
    it(lessonDir, () => {
      const authored = JSON.parse(readFileSync(join(__dirname, "../authored/quick-checks", `${lessonDir}.json`), "utf8"));
      const idx = JSON.parse(readFileSync(join(base, lessonDir, "index.json"), "utf8"));
      expect(idx.sections).toHaveLength(authored.items.length);
      expect(idx.groups.every((g) => g.question_count >= 1 && g.question_count <= 3)).toBe(true);
      expect(idx.groups.reduce((n: number, g) => n + g.question_count, 0)).toBe(authored.items.length);
      for (let i = 0; i < idx.sections.length; i++) {
        const row = idx.sections[i];
        const item = authored.items[i];
        expect(row.placement_after_grammar_refs).toEqual(item.grammar_refs);
        const storage = JSON.parse(readFileSync(join(base, lessonDir, row.storage_file), "utf8"));
        const [loaded] = sectionsFromLessonExerciseContent(storage.format, JSON.stringify(storage.content));
        expect(sectionAdminKind(loaded)).toBe(item.kind);
        expect(loaded.questions[0].explanation).toBe(item.explanation_vi);
        if (item.kind === "manualQnA") {
          const answerFromRawId = item.choices.find((c: { id: string; text: string }) => c.id === item.correct)?.text;
          expect(answerFromRawId).toBeTruthy();
          expect(loaded.questions[0].choices.find((c) => c.id === loaded.questions[0].correctChoiceId)?.text).toBe(answerFromRawId);
          expect(row.paste_file).toBeNull();
        } else {
          expect(loaded.questions[0].blankAnswers?.[0]?.text).toBe(item.correct);
        }
      }
    });
  }
});

describe("direct B drill adaptations", () => {
  const base = join(__dirname, "../exports/curriculum-exercises/renshuu-drills");
  const src = join(__dirname, "../authored/renshuu-drills");
  for (const file of readdirSync(src).filter((name) => /^lesson-\d\d\.json$/.test(name))) {
    const dir = join(base, file.slice(0, -5));
    it(file, () => {
      const authored = JSON.parse(readFileSync(join(src, file), "utf8"));
      const index = JSON.parse(readFileSync(join(dir, "index.json"), "utf8"));
      expect(index.sections.map((row) => row.id)).toEqual(authored.items.map((q) => q.id + ".section"));
      for (const [i, section] of index.sections.entries()) {
        const item = authored.items[i];
        const storage = JSON.parse(readFileSync(join(dir, section.storage_file), "utf8"));
        const [first] = sectionsFromLessonExerciseContent(storage.format, JSON.stringify(storage.content));
        const [saved] = sectionsFromLessonExerciseContent(storage.format, serializeSectionContent(first));
        expect(sectionAdminKind(saved)).toBe(item.kind);
        const [q] = saved.questions;
        expect(q.explanation).toBe(item.explanation_vi);
        if (item.kind === "manualFillInBlank") {
          expect(q.blankAnswers.map((b) => b.text)).toEqual([item.correct]);
        } else {
          const expectedIds = Array.isArray(item.correct) ? item.correct : [item.correct];
          const actualIds = item.kind === "manualMultiSelect" ? q.correctChoiceIds : [q.correctChoiceId];
          expect(q.choices.map((choice) => choice.text)).toEqual(item.choices.map((choice) => choice.text));
          expect(q.choices.filter((choice) => actualIds.includes(choice.id)).map((choice) => choice.text))
            .toEqual(item.choices.filter((choice) => expectedIds.includes(choice.id)).map((choice) => choice.text));
        }
      }
    });
  }
});
