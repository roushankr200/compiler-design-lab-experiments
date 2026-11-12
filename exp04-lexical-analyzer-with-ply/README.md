# Experiment 4 - Lexical Analyzer with PLY

Install first: `pip install ply`

| File | Question |
|---|---|
| q1_ply_lexer_identifiers_numbers_operators.py | Q1. PLY lexer for identifiers, numbers (int + float), arithmetic operators (+ - * /) and assignment (=) |
| q2_ply_ignore_whitespace_comments.py | Q2. Ignore whitespace/tabs and // and /* */ comments |
| q3_ply_identifier_length_limit.py | Q3. Identifier length restricted to 10 characters, error message if exceeded |
| q4_ply_tokens_to_separate_files.py | Q4. Store tokens in keywords.txt / identifiers.txt / operators.txt / numbers.txt |
| q5_ply_lexical_error_handling.py | Q5. Lexical error handling - illegal character, line + column printed, character skipped, scanning continues |

Note: only the questions were supplied for this experiment (no ready code),
so these programs were written to those questions.

Run: `python3 q1_ply_lexer_identifiers_numbers_operators.py` (etc.)
PLY generates lextab.py / parser.out in the run folder - harmless, can be deleted.
