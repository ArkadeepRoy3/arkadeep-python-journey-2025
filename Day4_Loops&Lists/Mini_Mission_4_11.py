'''
🔍 Mini Mission 11: List Filter – Evens Only
📌 Goal:
Take a list of numbers from the user and create a new list containing only the even numbers.

🔧 What You'll Practice:
List creation using a loop
Using if condition to filter
Creating a new list based on conditions
'''

original_list = []
even_list = []

numbers = int(input("How many numbers would you like to enter?: "))

for i in range(numbers):
    number = int(input(f"Enter number {i+1}: "))
    original_list.append(number)

print(f"📦 Original List: {original_list}")

for i in range(numbers):
    if original_list[i] % 2 == 0:
        even_list.append(original_list[i])

'''
Alternate:

for number in original_list:
    if number % 2 == 0:
        even_list.append(number)
'''

print(f"🧮 Even Numbers Only: {even_list}")