'''
🧩 Task:
Write a Python script that:

Asks the user to enter:
A number (as a string)
A word (like "hello")
A decimal number

Then:

Convert the number to an int
Convert the decimal to an int
Concatenate the number (as string) and word
Repeat the word 3 times (but in uppercase)
Multiply the two integer values (converted number and decimal)
'''

number = input("Enter a number:")
word = input("Enter a word:")
decimal = float(input("Enter a decimal:"))

num_to_int = int(number)
deci_to_int = int(decimal)

print(f"Concatenated string: {number+word}")
print(f"Repeated word: {word.upper()*3}")
print(f"Decimal converted to int and multiplied: {num_to_int*deci_to_int}")