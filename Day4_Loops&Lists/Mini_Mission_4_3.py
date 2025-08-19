'''
🧪 Mini Mission 3 - Sum of N Numbers
🎯 Your Goal:
Take a number N from the user and print the sum of the first N natural numbers using a while loop.
'''

number = int(input("Please enter the value of N:"))
total = 0

for i in range(number+1):
    total += i

print(f"N = {number}")
print(f"Output: {total}")


#Using while loop

number = int(input("Enter the value of N:"))
total = 0
i = 1

while i <= number:
    total += i
    i += 1

print(f"N = {number}")
print(f"Output: {total}")

#Bonus Formula:

number = int(input("Enter the value of N:"))

total = number * (number + 1)//2

print(f"N = {number}")
print(f"Output: {total}")
