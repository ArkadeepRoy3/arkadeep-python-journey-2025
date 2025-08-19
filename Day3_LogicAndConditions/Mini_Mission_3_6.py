'''
🎮 Mini Mission 6: Number Comparison Game
Goal: Build a smart number comparison tool using user input and conditional logic.

🔍 Problem Statement:

Ask the user to enter two numbers.

Then:

Check and display which number is greater.
If both are equal, print a message saying so.
Add a fun twist: also print the difference between the two numbers.
'''
import math

num1 = int(input("Please input the 1st number:"))
num2 = int(input("Please input the 2nd number:"))

if num1 == num2:
    print("Both numbers are equal!")
else:
    if num1 > num2:
        print(f"{num1} number is greater than {num2}!")
    else:
        print(f"{num2} number is greater than {num1}!")

print(f"The difference between the two numbers is {abs(num1-num2)}")