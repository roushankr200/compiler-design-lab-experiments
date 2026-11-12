# Q3. Delete specified line numbers from a text file.

def delete_lines(filename, remove_lines):
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for i, line in enumerate(lines, start=1):
            if i not in remove_lines:
                f.write(line)


delete_lines("input.txt", [3, 6])
print("Specified lines removed successfully.")
