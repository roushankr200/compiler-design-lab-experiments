# Experiment 2 - Operator Validation using Lexical Analysis
# Lexical analyzer that finds operators in a source code file and
# classifies each one as VALID or INVALID using predefined lexical rules.
#
# Valid operators are grouped by category. Any operator-like symbol
# sequence that is not in the valid set is reported as INVALID.

import re

VALID_OPERATORS = {
    # Arithmetic
    '+': 'Arithmetic', '-': 'Arithmetic', '*': 'Arithmetic',
    '/': 'Arithmetic', '%': 'Arithmetic', '**': 'Arithmetic', '//': 'Arithmetic',
    # Relational / Comparison
    '==': 'Relational', '!=': 'Relational', '>': 'Relational',
    '<': 'Relational', '>=': 'Relational', '<=': 'Relational',
    # Logical (symbol form)
    '&&': 'Logical', '||': 'Logical', '!': 'Logical',
    # Assignment
    '=': 'Assignment', '+=': 'Assignment', '-=': 'Assignment',
    '*=': 'Assignment', '/=': 'Assignment', '%=': 'Assignment',
    # Bitwise
    '&': 'Bitwise', '|': 'Bitwise', '^': 'Bitwise', '~': 'Bitwise',
    '<<': 'Bitwise', '>>': 'Bitwise',
}

# Word-form logical operators
WORD_OPERATORS = {'and': 'Logical', 'or': 'Logical', 'not': 'Logical'}

# Longest operator-like sequences first, so >= is read as one token, not > and =
OPERATOR_PATTERN = re.compile(r'\*\*=|//=|\*\*|//|==|!=|>=|<=|<>|=<|=>|&&|\|\||\+=|-=|\*=|/=|%=|<<|>>|[+\-*/%=<>!&|^~@#$?\\]|\b(?:and|or|not)\b')


def validate_operators(filename):
    with open(filename, 'r') as f:
        code = f.read()

    print(f"{'Operator':<12}{'Category':<14}{'Result'}")
    print("-" * 42)
    valid_count = invalid_count = 0
    for match in OPERATOR_PATTERN.finditer(code):
        op = match.group()
        if op in VALID_OPERATORS:
            print(f"{op:<12}{VALID_OPERATORS[op]:<14}Valid")
            valid_count += 1
        elif op in WORD_OPERATORS:
            print(f"{op:<12}{WORD_OPERATORS[op]:<14}Valid")
            valid_count += 1
        else:
            print(f"{op:<12}{'-':<14}Invalid")
            invalid_count += 1
    print("-" * 42)
    print("Total Valid Operators:", valid_count)
    print("Total Invalid Operators:", invalid_count)


validate_operators("source_code.txt")
