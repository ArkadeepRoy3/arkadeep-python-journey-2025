'''
🧪 Mini Mission 4: Smart Number Filter
🎯 Mission Goals:

Use for loop with range()
Apply if conditions inside loops
Use continue to skip unwanted numbers

🔧 Problem Statement:
Write a program that:

Asks the user to enter a number N.
Then prints all numbers from 1 to N that are:
Divisible by 3, but
Skip numbers that are also divisible by 5 (use continue)
'''

number = int(input("Please enter a number:"))

for i in range(1, number+1):
    if i % 5 == 0:
        continue
    elif i % 3 == 0:
        print(i)

# Alternate

number = int(input("Please enter a number:"))

for i in range(1, number+1):
    if i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 3 == 0:
        print(i)