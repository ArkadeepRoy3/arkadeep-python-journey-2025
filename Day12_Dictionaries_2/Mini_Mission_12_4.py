'''
🧩 Mini Mission 4: Reverse Lookup

Goal: Given a dictionary of student names and grades, allow the user to search by grade and print all students who have that grade.

✅ Requirements:

Ask the user to input a grade.
Find all students with that exact grade.
If none found, print a message.
Handle non-integer input gracefully (optional challenge).

🧾 Example Run:

Enter grade to search: 90  
Students with grade 90: Ria, Nina

Enter grade to search: 85  
Students with grade 85: Arka, John

Enter grade to search: 75  
❌ No student found with that grade.

🧪 Sample Dictionary:

grades = {
    "arka": 85,
    "ria": 90,
    "samit": 78,
    "john": 85,
    "nina": 90
}
'''
def rev_lookup(grades):
    grade = int(input("Enter a grade: "))
    
    if grade not in grades.values():
        print("❌ No student found with that grade.")
    for student in grades:
        if grades[student] == grade:
            print(f"Student with grade {grade}: {student.title()}")
    
grades = {
    "arka": 85,
    "ria": 90,
    "samit": 78,
    "john": 85,
    "nina": 90
}

rev_lookup(grades)