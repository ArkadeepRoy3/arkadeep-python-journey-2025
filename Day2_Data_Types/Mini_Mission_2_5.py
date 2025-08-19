'''
Ask the user for three inputs:

A number
A decimal
A boolean (Yes/No)

Convert:

The number to an int
The decimal to a float
The boolean input to a Python boolean (True or False)

Print:

All three values with their data types
A final message that says whether all inputs were successfully processed
'''

number = input("Enter a number:")
decimal = input("Enter a decimal:")
boolean = input("Enter Yes or No (boolean):")

num_to_int = int(number)
deci_to_float = float(decimal)
if boolean.lower() == "yes":
    booltxt_to_bool = True
else:
    booltxt_to_bool = False

print(f"Value of number is {num_to_int} and type is : {type(num_to_int)}")
print(f"Value of decimal is {deci_to_float} and type is : {type(deci_to_float)}")
print(f"Value of boolean is {booltxt_to_bool} and type is : {type(booltxt_to_bool)}")
print("All inputs processed successfully!")