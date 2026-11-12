# Experiment 2 - Operator Validation using Lexical Analysis

Objective: simulate a lexical analyzer, identify operators in a source code
file, and classify them as valid / invalid using predefined lexical rules.

| File | What it is |
|---|---|
| operator_validation.py | The program - scans source_code.txt, prints each operator with its category (Arithmetic / Relational / Logical / Assignment / Bitwise) and Valid or Invalid |
| source_code.txt | Sample source file - contains valid operators plus `<>`, `=<` and `@` which must come out Invalid |

Note: only the assignment objective was supplied for this experiment (no ready
code), so this program was written to that objective. Valid set = common
Python/C-style operators; anything operator-like outside the set is Invalid.

Run: `python3 operator_validation.py`
