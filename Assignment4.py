class Student:

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks


students = []


# CREATE
def create_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    student = Student(roll, name, marks)
    students.append(student)

    print("Student added successfully!")


# READ
def read_student():
    if len(students) == 0:
        print("No students found!")
    else:
        for student in students:
            print("Roll No:", student.roll)
            print("Name:", student.name)
            print("Marks:", student.marks)
        


# UPDATE
def update_student():
    roll = int(input("Enter Roll No to update: "))

    for student in students:
        if student.roll == roll:
            student.name = input("Enter New Name: ")
            student.marks = int(input("Enter New Marks: "))

            print("Student updated!")
            return

    print("Student not found!")


# DELETE
def delete_student():
    roll = int(input("Enter Roll No to delete: "))

    for student in students:
        if student.roll == roll:
            students.remove(student)
            print("Student deleted!")
            return

    print("Student not found!")


# MENU
while True:

    print("\nStudent Management System ")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        create_student()

    elif choice == 2:
        read_student()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid choice!")