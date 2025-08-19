'''
Divisibility Checker
📥 Input:
Ask the user to enter a number.

🎯 Task:

If divisible by both 3 and 5, print "FizzBuzz".
If divisible by only 3, print "Fizz".
If divisible by only 5, print "Buzz".
If divisible by neither, print "Not divisible by 3 or 5".
'''

number = float(input("Enter a number:"))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Not divisible by 3 or 5")