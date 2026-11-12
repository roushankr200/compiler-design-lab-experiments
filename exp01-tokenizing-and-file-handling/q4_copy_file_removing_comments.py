# Q4. Copy contents from one file to another after removing comments
#     (lines starting with #).

def copy_clean(src, dest):
    with open(src, 'r') as s, open(dest, 'w') as d:
        for line in s:
            if not line.strip().startswith("#"):
                d.write(line)


copy_clean("source.txt", "destination.txt")
print("File copied after removing comments.")
