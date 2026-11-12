# Experiment 5 - Scanner Implementation using Lark Parser

Scanner for a mini language: tokenizes identifiers, numbers, operators,
delimiters and keywords, ignores whitespace and comments, reports token
positions, handles errors, and stores categorized tokens into files.
Install first: `pip install lark`

| File | Question |
|---|---|
| q1_lark_tokenization_ebnf.py | Q1. Tokenization using an EBNF grammar |
| q2_lark_ignore_whitespace_comments.py | Q2. Ignoring whitespace and // /* */ comments |
| q3_lark_line_column_reporting.py | Q3. Line and column number reporting for tokens |
| q4_lark_error_handling_recovery.py | Q4. Custom error handling and recovery (missing semicolon) |
| q5_lark_token_categorization_files.py | Q5. Token categorization + storage in identifiers/numbers/operators/keywords .txt files with frequencies |

Two small fixes vs the handout, marked NOTE in the files, so the sample data
actually parses: Q1 statement allows an optional KEYWORD (int x = 10;),
Q2 start allows more than one assignment (the sample has two statements).

Run: `python3 q1_lark_tokenization_ebnf.py` (etc.)

Verified outputs differ from the handout samples in two places (the code here
is the verified one): Q4 reports the error at column 8, not 7 - that is where
the unexpected `y` actually is. Q5 Identifier Frequency is {'x': 4}, not 3 -
the sample data contains four `x` identifiers.
