'''
Simple Calculator
🧩 Problem Statement:
Write a simple calculator that:

Asks the user to input two numbers.
Asks the user to choose an operation (+, -, *, /, //, %, **)
Performs the chosen operation.
Handles invalid choices gracefully.
'''

num1 = int(input("Please enter 1st number:"))
num2 = int(input("Please enter 2nd number:"))

choice = input("Please choose one of the following operations ((+, -, *, /, //, %, **):")

if choice == "+":
    print(f"Addition: {num1+num2}")
elif choice == "-":
    print(f"Subtraction: {num1-num2}")
elif choice == "*":
    print(f"Multiplication: {num1*num2}")
elif choice == "/":
    if num2 != 0:
        print(f"Division: {num1/num2}")
    else:
        print("Cannot divide by zero.")
elif choice == "//":
    if num2 != 0:
        print(f"Floor Division: {num1//num2}")
    else:
        print("Cannot divide by zero.")
elif choice == "%":
    if num2 != 0:
        print(f"Modulus: {num1%num2}")
    else:
        print("Cannot divide by zero.")
elif choice == "**":
    print(f"Exponentiation: {num1**num2}")
else:
    print("Please choose a valid operation from the options!")