'''
Grading System
📝 Task:
Write a program that takes a student's marks as input (out of 100), and based on the score, prints their grade using the following logic:

Marks Range	Grade
90 - 100	A+
80 - 89	    A
70 - 79	    B
60 - 69	    C
50 - 59	    D
Below 50	F

🧠 Instructions:

Ask the user to enter their marks.
Convert the input to integer.
Use if-elif-else statements to assign a grade.

Print out a sentence like:
You scored 85 and your grade is A.
'''

marks = int(input("Please enter your marks (0-100):"))

if 0 <= marks <= 100:
    if 90 <= marks <= 100:
        print(f"You scored {marks} and your grade is A+")
    elif 80 <= marks <= 89:
        print(f"You scored {marks} and your grade is A")
    elif 70 <= marks <= 79:
        print(f"You scored {marks} and your grade is B")
    elif 60 <= marks <= 69:
        print(f"You scored {marks} and your grade is C")
    elif 50 <= marks <= 59:
        print(f"You scored {marks} and your grade is D")
    else: 
        print(f"You scored {marks} and your grade is F")
else:
     print("Invalid input. Marks should be between 0 and 100.")