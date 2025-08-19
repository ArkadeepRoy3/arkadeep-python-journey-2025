'''
🧩 Mini Mission 3: Smart Dictionary Tools

You'll work with a dictionary of students and their grades. Your job is to create a CLI menu with 4 operations using the dictionary methods listed below.

✅ Your Mission Menu — Implement:

Search Student Grade - Use get() to safely fetch the grade of a student entered by the user.
Add Student with Default Grade - Use setdefault() to add a student. Default grade is 50 if no grade given.
Update Grades - Use update() to change the grade of an existing student.
Remove Student - Use pop() to remove a student from the dictionary.

Each action should:

Prompt the user for input
Perform the action using the correct dictionary method
Print a helpful success/failure message
And finally:
Use a loop so the user can keep using the tool
Add an “Exit” option

💡 Example Interaction

What would you like to do?
1. Search Student Grade
2. Add Student with Default Grade
3. Update Grades
4. Remove Student
5. Exit
Enter choice: 1
Enter student name: ria
✅ Ria's grade: 90

📝 The Dictionary

grades = {
    "arka": 85,
    "ria": 90,
    "samit": 78
}
'''

def search_student_grade(grades):
    search_input = input("Enter student name: ").lower().strip()
    grade = grades.get(search_input)
    if grade is not None:
        print(f"{search_input.title()}'s grade: {grade}")
    else:
        print("❌ Student not found.")

def add_student(grades):
    new_student = input("Enter the name of new student: ").lower().strip()
    new_student_grade = int(input("Enter the grade of the new student: "))
    if new_student in grades:
        print("Student is already present.")
    else:
        if new_student_grade == 0 or new_student_grade == None:
            grades[new_student] = 50
        else:
            grades[new_student] = new_student_grade
    for student in grades:
        print(f"{student.title()} : {grades[student]}")

def update_grades(grades):
    student_name = input("Enter the name of student to update their grade: ").lower().strip()
    grade = int(input("Enter the new grade of the student: "))
    for student in grades:
        if student_name == student:
            grades.update({student : grade})
    for student in grades:
        print(f"{student.title()} : {grades[student]}")

def remove_student(grades):
    student_name = input("Enter the student name to remove them: ").lower().strip()
    if student_name not in grades:
        print("Student not found.")
    else:
        grades.pop(student_name)
    for student in grades:
        print(f"{student.title()} : {grades[student]}")

def sdt_menu(grades):
    while True:
        print("What would you like to do?")
        print("1. Search Student Grade")
        print("2. Add Student with Default Grade")
        print("3. Update Grades")
        print("4. Remove Student")
        print("5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            search_student_grade(grades)
        elif choice == "2":
            add_student(grades)
        elif choice == "3":
            update_grades(grades)
        elif choice == "4":
            remove_student(grades)
        elif choice == "5":
            return
        else:
            print("Choose among the given options.")
    

grades = {
    "arka": 85,
    "ria": 90,
    "samit": 78
}

sdt_menu(grades)