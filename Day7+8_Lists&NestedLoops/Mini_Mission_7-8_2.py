'''
🧪Mini Mission 2: Student Marks Analyzer
🎯 Your Tasks:

📥 Ask the user how many student marks to input.
📝 Accept all marks (as integers) and store them in a list.
🧮 Display:

Total number of students
Average mark
Highest mark
Lowest mark

🏅 Use if-else to assign a grade to the class based on the average:

90-100: A+
80-89: A
70-79: B
60-69: C
50-59: D
Below 50: F
'''

'''def student_mark_analyzer():
    student_marks = []
    number = int(input("How many students?: "))
    for i in range(number):
        marks = int(input(f"Enter mark for student {i+1} (0-100): "))
        student_marks.append(marks)

    print("📊 Class Statistics:")
    print(f"- Total Number of Students: {len(student_marks)}")
    average_marks = sum(student_marks)/(len(student_marks))
    print(f"- Average Marks of students: {int(average_marks)}")
    highest_marks = max(student_marks)
    index_high = student_marks.index(highest_marks)
    print(f"- Highest Marks is : {highest_marks} and scored by Student {index_high+1}")
    lowest_marks = min(student_marks)
    index_low = student_marks.index(lowest_marks)
    print(f"- Lowest Marks is : {lowest_marks} and scored by Student {index_low+1}")
    if 0 <= average_marks <= 100:
        if average_marks >= 90:
            print("- Grade: A+")
        elif average_marks >= 80:
            print("- Grade: A")
        elif average_marks >= 70:
            print("- Grade: B")
        elif average_marks >= 60:
            print("- Grade: C")
        elif average_marks >= 50:
            print("- Grade: D")
        else:
            print("- Grade: F") 

print(student_mark_analyzer())'''

# A different version

def get_student_marks():
    student_marks = []
    count = int(input("How many students?: "))
    for i in range(count):
        mark = int(input(f"Enter mark for student {i+1} (0-100): "))
        student_marks.append(mark)
    return student_marks

def calculate_stats(marks):
    total = len(marks)
    avg = sum(marks) / total
    highest = max(marks)
    lowest = min(marks)
    highest_index = marks.index(highest)
    lowest_index = marks.index(lowest)
    return total, avg, highest, lowest, highest_index, lowest_index

def determine_grade(average):
    if 90 <= average <= 100:
        return "A+"
    elif 80 <= average < 90:
        return "A"
    elif 70 <= average < 80:
        return "B"
    elif 60 <= average < 70:
        return "C"
    elif 50 <= average < 60:
        return "D"
    else:
        return "F"

def display_report():
    marks = get_student_marks()
    total, avg, high, low, high_idx, low_idx = calculate_stats(marks)
    grade = determine_grade(avg)

    print("\n📊 Class Statistics:")
    print(f"- Total Students: {total}")
    print(f"- Average Mark: {avg:.2f}")
    print(f"- Highest Mark: {high} (Student {high_idx+1})")
    print(f"- Lowest Mark: {low} (Student {low_idx+1})")
    print(f"- Grade: {grade}")

display_report()