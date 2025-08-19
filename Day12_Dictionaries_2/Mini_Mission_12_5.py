'''
🧩 Mini Mission 5: Dict Visualizer

🎯 Objective:
Write a function that prints a dictionary in a clean, formatted way — like a table.

🛠️ Requirements:

Accept a dictionary of student names and their grades.
Print them in a visually clean table format.
Use alignment and formatting (f-strings, .ljust(), etc.) to make it look nice.
Use a function named visualize_dict(data: dict)

🧪 Example:

grades = {
    "arka": 85,
    "ria": 90,
    "samit": 78,
    "john": 85,
    "nina": 90
}

visualize_dict(grades)

✅ Expected Output:

Student     | Grade
--------------------
Arka        | 85
Ria         | 90
Samit       | 78
John        | 85
Nina        | 90
'''
def visualize(grades):
    print("Student     | Grade")
    print("--------------------")
    for student, grade in grades.items():
        print(f"{student.title():<12}| {grade}")

grades = {
    "arka": 85,
    "ria": 90,
    "samit": 78,
    "john": 85,
    "nina": 90
}

visualize(grades)