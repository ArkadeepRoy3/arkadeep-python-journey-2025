'''
🧪 Mini Mission 1 – Countdown Timer
🎯 Your Task:
Write a Python program that:

Takes a number as input (e.g., 10)
Counts down to 0 using a while loop
Prints “Blast Off! 🚀” when it hits 0
'''

number = int(input("Enter number for countdown:"))

while number >= 0:
    print(number)
    number -= 1
print("Blast Off! 🚀")