# Q5. Basic lexical analyzer that identifies tokens:
#     Keyword / Identifier / Literal / Operator / Delimiter.

import keyword
import re


def lexical_analysis(filename):
    with open(filename, 'r') as f:
        code = f.read()

    tokens = re.findall(r'\b\w+\b|[+\-*/%=<>(),]', code)

    for token in tokens:
        if keyword.iskeyword(token):
            print(token, "-> Keyword")
        elif token.isidentifier():
            print(token, "-> Identifier")
        elif token.isnumeric():
            print(token, "-> Literal")
        elif token in "+-*/%=<>":
            print(token, "-> Operator")
        else:
            print(token, "-> Delimiter")


lexical_analysis("program.py")
