# Q1. Analyze a text file and report: number of lines, words,
#     characters (excluding whitespace) and blank lines.

def analyze_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if line.strip() == "")
    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line.replace(" ", "").replace("\n", "")) for line in lines)

    print("Lines:", total_lines)
    print("Blank Lines:", blank_lines)
    print("Words:", total_words)
    print("Characters:", total_chars)


analyze_file("input.txt")
