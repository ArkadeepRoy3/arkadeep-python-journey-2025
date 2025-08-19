'''
🧩 Mini Mission 6: Dictionary Debugger

🛠️ Problem:

You're given a dictionary of student grades, but due to some errors in data entry, a few values are invalid or inconsistent.
Your task is to detect and clean the data using logic. Specifically:
Remove any student whose grade is not an integer (e.g., "N/A", None, "absent").
If the grade is an integer but negative or above 100, correct it to the nearest valid range (minimum 0, maximum 100).
Print the cleaned dictionary neatly using your own format (you can reuse the visualizer style from Mini Mission 5 if you want).
'''
def dict_debugger(grades):
    print("🧼 Cleaned Grades:")
    for student, grade in grades.items():
        if isinstance(grade, int):
            if grade < 0:
                grade = 0
            elif grade > 100:
                grade = 100
            print(f"{student.title():<12}| {grade}")

grades = {
    "arka": 85,
    "ria": "N/A",
    "samit": 105,
    "john": 78,
    "nina": -10,
    "dev": None,
    "tara": 90,
    "ram": "absent"
}

dict_debugger(grades)