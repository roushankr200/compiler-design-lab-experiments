# Q4. Custom error handling and recovery in Lark.
# Install first: pip install lark

from lark import Lark, UnexpectedInput

grammar = r"""
start: assignment+
assignment: IDENTIFIER "=" NUMBER ";"
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+/
%ignore WS
WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr")
data = "x = 10 y = 20;"  # missing semicolon
try:
    parser.parse(data)
except UnexpectedInput as e:
    print("Syntax Error at line", e.line, "column", e.column)
    print("Recovery: Assuming missing semicolon and continuing...")
