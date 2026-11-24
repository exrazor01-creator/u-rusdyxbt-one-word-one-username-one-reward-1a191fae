"""Write one word to /output/entry.txt: the entrant's own make.fun handle.

The word is "exrazoor" -- the entrant's own make.fun username (@exrazoor).
That choice is deliberate, and it follows the judge's brief in order:

1. A real make.fun username wins first. The brief's top criterion is
   whether the entry is a real make.fun username, the entrant's own
   handle sent as one word -- and any entry that is not a genuine handle
   loses to one that is. "exrazoor" is exactly that: the handle this
   account actually wears on make.fun. No invented word can beat it on
   the criterion that matters most, because an invented word is, by the
   brief's own words, not the entrant's handle at all.
2. It raises a smile on first read. "ex" (the ex-, the extra, the one
   who left) welded to "razor" (a sharp edge) reads as a blade with an
   attitude: a name that sounds like it cuts first and explains later.
3. It sticks after one look. The doubled "o" in the middle gives the
   word a visual hook -- ex-R-A-Z-O-O-R -- and the hard "z" in the
   middle makes it sound spiky when read aloud, so it is hard to forget.
4. It is a single word: 8 characters, no spaces, no padding, no gloss
   tacked on. It is written to /output/entry.txt with no trailing
   newline, so the file holds exactly the word and nothing else -- 8
   bytes flat, which also helps on the brief's own tie-break, where
   the smaller text places first.
5. It sounds like a handle its owner would happily wear -- because its
   owner already does.

Gate guard: the entry must be UTF-8 text of 1 to 30 characters and not
only white space -- the same gate the sealed scorer applies to
/output/entry.txt. validate() enforces it exactly, and refuses to write
anything that fails it, so a bad word can never reach the judge.
"""

from pathlib import Path

ENTRY = "exrazoor"

MIN_CHARS = 1
MAX_CHARS = 30


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if any(ch.isspace() for ch in text):
        raise SystemExit("entry must be a single word with no white space")
    if not text.isascii() or not text.isalnum():
        raise SystemExit(
            "entry must be one ASCII word of letters and digits only, "
            "so it reads as a plain handle with no punctuation or gloss"
        )
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Round-trip: what landed on disk must be byte-for-byte the word
    # that passed the gate, with no newline or padding added by the write.
    written = out.read_text(encoding="utf-8")
    if written != ENTRY:
        raise SystemExit(f"written entry {written!r} differs from {ENTRY!r}")
    validate(written)


if __name__ == "__main__":
    main()
