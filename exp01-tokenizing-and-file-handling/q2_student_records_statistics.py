# Q2. Store student records in a file and compute class statistics
#     (average, highest and lowest marks).

def student_data():
    n = int(input("Enter number of students: "))
    records = []

    for _ in range(n):
        roll = input("Roll No: ")
        name = input("Name: ")
        marks = float(input("Marks: "))
        records.append((roll, name, marks))

    with open("students.txt", "w") as f:
        for r in records:
            f.write(f"{r[0]} {r[1]} {r[2]}\n")

    marks_list = [r[2] for r in records]
    print("Average Marks:", sum(marks_list) / n)
    print("Highest Marks:", max(marks_list))
    print("Lowest Marks:", min(marks_list))


student_data()
