'''
🧪 Mini Mission 5 – Grading System
Concepts: Functions, logic, conditionals

🎯 Task:
Write a program that:
Takes a score (0-100) from the user

Returns a grade based on the score:

90-100 → A+
80-89 → A
70-79 → B
60-69 → C
50-59 → D
Below 50 → F
'''

def grading_system():
    grade = int(input("Please enter your test score (out of 100): "))
    if grade >= 0 and grade <= 100:
        if 90 <= grade <= 100:
            return "A+"
        elif 80 <= grade <= 89:
            return "A"
        elif 70 <= grade <= 79:
            return "B"
        elif 60 <= grade <= 69:
            return "C"
        elif 50 <= grade <= 59:
            return "D"
        else:
            return "F"
    else:
        return "Please enter a valid grade!"

result = grading_system()
print(result)