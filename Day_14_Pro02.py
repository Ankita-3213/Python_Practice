import math

subjects = ("Physics", "Maths", "Chemistry", "Biology", "PE")
students = []

cal_percentage = lambda total, count: total/count

def add_student():
    name = input("Enter name of student: ")
    marks = []
    total = 0

    for sub in subjects:
        mark= float(input(f"Enter marks for {sub}: "))
        marks.append(mark)
        total = total + mark
    percentage = cal_percentage(total, len(subjects))
    student = {"name":name, "marks":marks, "percentage":percentage}
    students.append(student)
    print("Student added successfully !\n")

def show_result():
    for student in students:
        print("\nName:",student["name"])
        for i in range(len(subjects)):
            print(f"{subjects[i]}: {student['marks'][i]}")
        print("Percentage:",student["percentage"])


while True:
    print("\n1. Add Student")
    print("2. Show result")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_result()
    elif choice == "3":
        print("Thank you")
        break
    else:
        print("Enter 1 or 2 or 3")
        