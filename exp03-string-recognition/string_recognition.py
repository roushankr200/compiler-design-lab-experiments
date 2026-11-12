# Experiment 3 - String Recognition
# Recognize strings matching the regular expressions:
#   1) a*     -> zero or more 'a' (also matches the empty string)
#   2) a*b+   -> zero or more 'a' followed by one or more 'b'
#   3) abb    -> exactly the string "abb"
# The program accepts input strings from the user and displays
# which pattern(s) each string matches.

import re

PATTERNS = {
    'a*': re.compile(r'a*'),
    'a*b+': re.compile(r'a*b+'),
    'abb': re.compile(r'abb'),
}


def recognize(string):
    matched = [name for name, pattern in PATTERNS.items()
               if pattern.fullmatch(string)]
    if matched:
        print(f'"{string}" matches: {", ".join(matched)}')
    else:
        print(f'"{string}" matches: No pattern')


print("String Recognition for patterns: a* , a*b+ , abb")
print("Enter strings one by one. Press Enter on an empty line (or type 'exit') to stop.")

while True:
    s = input("Enter a string: ").strip()
    if s == "" or s.lower() == "exit":
        # An empty line stops input - but first show that a* matches the empty string
        if s == "":
            print('"" (empty string) matches: a*')
        break
    recognize(s)
