'''
🧪 Mini Mission 2 – Table Generator 📋
🎯 Goal: Print the multiplication table of any number up to 10
📌 Core Concepts:

for loop
range() function
String formatting for clean output
'''

number = int(input("Please enter the number for which you wish to print the multiplication table:"))

for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")