# SP Lab - Compiler / Lexical Analysis Experiments (All 6)

All 6 experiments in one download. Each folder is named by what the code does.

## Download everything in one command
```
wget <TINYURL> -O sp-lab-experiments.zip
unzip sp-lab-experiments.zip
```
Or from GitHub: https://github.com/roushankr200/compiler-design-lab-experiments
(clone it, or download the release zip)

## Index
| Folder | Experiment | Contents |
|---|---|---|
| exp01-tokenizing-and-file-handling/ | Exp 1 - Concept of Tokenizing & File Handling | 6 programs: file statistics, student records, delete lines, copy without comments, basic lexical analyzer, remove forbidden words |
| exp02-operator-validation-lexical-analysis/ | Exp 2 - Operator Validation using Lexical Analysis | 1 program: finds operators in a source file, classifies Valid / Invalid with category |
| exp03-string-recognition/ | Exp 3 - String Recognition | 1 program: checks input strings against a*, a*b+, abb |
| exp04-lexical-analyzer-with-ply/ | Exp 4 - Lexical Analyzer with PLY | 5 programs: basic PLY lexer, ignore whitespace/comments, identifier length limit, tokens to separate files, lexical error handling with line/column |
| exp05-scanner-using-lark-parser/ | Exp 5 - Scanner Implementation using Lark Parser | 5 programs: EBNF tokenization, ignore whitespace/comments, line/column reporting, error handling/recovery, token categorization to files |
| exp06-dfa-from-regular-expression/ | Exp 6 - DFA Creation and Simulation from Regular Expression | 3 programs: DFA simulation for a*b, NetworkX visualization, Graphviz visualization |

## Setup
Python 3.8+ is enough for Exp 1-3. For Exp 4-6 install the libraries:
```
pip install -r requirements.txt
```
Exp 6 Q3 (Graphviz) also needs the Graphviz program itself installed on the
system (e.g. `sudo apt install graphviz` on Linux, or the Graphviz installer on Windows).

Every program was run and verified before upload. Each experiment folder has
its own README with the question list and how to run each file.
