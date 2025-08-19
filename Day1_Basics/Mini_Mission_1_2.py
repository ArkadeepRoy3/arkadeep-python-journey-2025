'''
Write a program that:

Asks for two numbers (from the user)
Adds them, subtracts them, multiplies them, divides them
Prints the result in a clean way using f-strings 
'''

num1 = input("Enter first number:")
num2 = input("Enter second number:")
print("Before conversion:", type(num1))
print("Before conversion:", type(num2))
num1 = int(num1)
num2 = int(num2)
print("After conversion:", type(num1))
print("After conversion:", type(num2))
add = num1 + num2
sub = num1 - num2
multiply = num1 * num2
div = num1 / num2
print(f"The result for addition is {add}, the result for subtraction is {sub}, the result for multiplying is {multiply}, and the result for divison is {div}.")