'''
🚀 Task:
Write a program that:

Asks the user to input their age.
Prints the correct category based on the above table.
🎯 Let’s keep it neat with chained comparisons and clean logic.
'''

age = int(input("Please enter your age:"))

if age < 0:
    print("Invalid age!")
elif 0 <= age <= 12:
    print("You fall into the Child category!")
elif 13 <= age <= 19:
    print("You fall into the Teenager category!")
elif 20 <= age <= 35:
    print("You fall into the Young Adult category!")
elif 36 <= age <= 59:
    print("You fall into the Adult category!")
elif 60 <= age <= 120:
    print("You fall into the Senior Citizen category!")
else:
    print("Age is too high to be true!")