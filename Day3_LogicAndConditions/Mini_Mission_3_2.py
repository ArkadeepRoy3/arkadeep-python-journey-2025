'''
Create a program that:

Takes one number as input
Calculates and displays:
Square root
Power of 2 (x²)
Power of 3 (x³)
Floor value
Ceil value
Absolute value
'''

import math

number = float(input("Enter a number:"))

if number >=0:
    print(f"Square root of the number is : {math.sqrt(number)}")
else:
    print("Square root not defined for negative numbers in real math.")
print(f"Square of the number (x²) is : {math.pow(number, 2)}")
print(f"Cube of the number (x³) is : {math.pow(number, 3)}")
print(f"Floor value of the number is : {math.floor(number)}")
print(f"Ceil value of the number is : {math.ceil(number)}")
print(f"Absolute value of the number is : {abs(number)}")