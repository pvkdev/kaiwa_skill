"""Source-preserving sentence boundaries used by JLPT editorial overlays and coverage."""

def sentence_units(text, quote_context=None):
    """Return source-preserving study units, keeping table rows and quoted/parenthetic speech together."""
    if "|" in text:
        return [text]
    closing = {"「": "」", "『": "』", "（": "）", "(": ")", "【": "】"}
    stack = [] if quote_context is None else quote_context
    parts = []
    start = 0
    for idx, char in enumerate(text):
        if char in closing:
            stack.append(closing[char])
        elif stack and stack[-1] == char:
            stack.pop()
        if char not in "。！？" or stack:
            continue
        rest = text[idx + 1:].lstrip()
        if not rest or rest[0] in "！？" or (char in "！？" and rest.startswith(("と", "って"))):
            continue
        parts.append(text[start:idx + 1].strip())
        start = idx + 1
    parts.append(text[start:].strip())
    return parts
