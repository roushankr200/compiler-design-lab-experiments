# Experiment 3 - String Recognition

Write a program to recognize strings that match: `a*`, `a*b+`, `abb`.
Accepts input strings from the user and displays which pattern(s) each matches.

| File | What it is |
|---|---|
| string_recognition.py | The program (uses re.fullmatch for each pattern) |

Quick check: `aaa` -> a* | `aab` -> a*b+ | `abb` -> a*b+ and abb | `b` -> a*b+ | `abc` -> no pattern

Note: only the assignment question was supplied for this experiment (no ready
code), so this program was written to that question.

Run: `python3 string_recognition.py`
