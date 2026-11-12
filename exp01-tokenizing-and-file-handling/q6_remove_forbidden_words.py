# Q6. Remove forbidden words from a file and generate a report
#     of how many times each forbidden word occurred.

from collections import Counter


def sanitize(source, drop, report):
    with open(drop, 'r') as f:
        forbidden = f.read().split()

    with open(source, 'r') as f:
        words = f.read().split()

    count = Counter(words)
    filtered = [w for w in words if w not in forbidden]

    with open(source, 'w') as f:
        f.write(" ".join(filtered))

    with open(report, 'w') as f:
        for word in forbidden:
            f.write(f"{word} : {count[word]} times\n")


sanitize("source.txt", "drop.txt", "report.txt")
print("Forbidden words removed and report generated.")
