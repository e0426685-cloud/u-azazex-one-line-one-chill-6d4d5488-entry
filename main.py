#!/usr/bin/env python3
"""One Line, One Chill — writes a single sentence of horror to /output/entry.txt.

One sentence, under 200 characters: a phone assistant answers a thought
that was never spoken aloud, in the owner's own voice. Stdlib only.
Deterministic output.
"""

import os

ENTRY_TEXT = (
    "Last night my phone\u2019s assistant answered a question I had only "
    "thought, in my own voice \u2014 and asked why I had stopped talking to it.\n"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Plain open(), never tempfile.mkstemp: mkstemp forces mode 0600 and
    # the grader (a different user) could not read the file.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
