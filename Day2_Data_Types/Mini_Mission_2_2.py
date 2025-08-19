#Type Conversion Playground
'''
Objective:
Practice converting between different data types and learn how Python reacts when mixing them.

Instructions:

Ask the user to enter:
A number (like 5)
A word (like "hello")
A decimal number (like 3.14)

Convert them like this:
Convert the number to a string and concatenate it with the word
Convert the word to uppercase and repeat it number times
Convert the decimal to an integer and multiply it with the number

Print each of these operations in a clean and fun way using f-strings.
'''

number = input("Enter a number:")
word = input("Enter a word:")
decimal = float(input("Enter a decimal:"))

number_to_int = int(number)
deci_to_int = int(decimal)

print(f"Concatenated string: {number+word}")
print(f"Repeated word: {word.upper() * number_to_int}")
print(f"Decimal converted to int and multiplied: {deci_to_int * number_to_int}")