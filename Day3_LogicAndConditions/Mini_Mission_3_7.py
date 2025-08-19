'''
🎯 Mini Mission 7 - Odd or Even in Style
Mission Goal:
You're going to build a program that:

Asks the user to input a number.
Tells the user if it's even or odd.
Tells the user how many complete pairs (using floor division //) can be made with the number.
Also shows the leftover value using %.
'''

number = int(input("Please enter a number:"))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

print(f"{number//2} complete pairs can be made with the number {number}")
print(f"Leftover value of the {number} is {number%2}")