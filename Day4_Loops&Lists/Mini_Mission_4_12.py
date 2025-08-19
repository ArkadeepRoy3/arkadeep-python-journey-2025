'''
🎯 Mission Goal:
You'll take a number from the user as a string, split it into individual digits, convert each to int, and store them in a list.

✅ Your Tasks:
Take a number input from the user (as string or input())

Loop through each character
Convert to int and store in a new list
Print the final list of digits
'''

digit_list = []
total = 0

number = input("Enter the number that you want to split: ")

for char in number:
    digit = int(char)
    digit_list.append(digit)

print(digit_list)

for i in range(len(digit_list)):
    total += digit_list[i]

print(f"Sum: {total}")