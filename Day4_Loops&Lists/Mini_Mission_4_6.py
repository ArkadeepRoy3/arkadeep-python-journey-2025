'''
🧪 Mini Mission 6: Topper Finder
🎯 Goal: Find the highest score from a list of student marks.

✅ Mission Objectives:
Use a list to store marks

Loop through the list to find the highest mark
Display the topper's score clearly
'''

marks = []

no_of_students = int(input("Enter the number of students:"))

index = 0
i = 1

while i <= no_of_students:
    temp = int(input(f"Enter the marks of student {i}:"))
    marks.append(temp)
    i += 1

max_marks = marks[0]
topper_index = 0

for i in range(len(marks)):
    if marks[i] > max_marks:
        max_marks = marks[i]
        topper_index = i

print(f"Topper of the class is student {topper_index+1} and their marks is {max_marks}")



'''
🎯 Topper Finder v2.0 – Feature List
We'll add:

✅ Highest mark (already done)
🏆 Name of the topper (not just “Student 1”)
👥 Multiple toppers if there's a tie
📋 Display of all marks in a nice format
'''

marks = []
names = []

no_stu = int(input("Enter the number of students: "))
i = 0

while i < no_stu:
    stu_names = input(f"Enter the name of the student {i+1}: ")
    stu_marks = int(input(f"Enter the marks of {stu_names}: "))
    marks.append(stu_marks)
    names.append(stu_names)
    i += 1

print("📋 Mark Sheet:")
for i in range(len(marks)):
    print(f"{names[i]}: {marks[i]}")

max_marks_a = marks[0]
topper_index_a = 0

for i in range(len(marks)):
    if marks[i] > max_marks_a:
        max_marks_a = marks[i]
        topper_index_a = i

topper = []

for i in range(len(marks)):
    if marks[i] == max_marks_a:
        topper.append(names[i])

if len(topper) == 1:
    print(f"\n🏆 Topper of the class is {topper[0]} with {max_marks_a} marks.")
else:
    print(f"\n🏆 Toppers of the class (tie with {max_marks_a} marks):")
    for name in topper:
        print(f"- {name}")