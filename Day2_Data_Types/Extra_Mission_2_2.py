'''
Leap Year Checker 🗓️💡

Build a simple program that:

Asks the user to enter a year (e.g., 2024)
Checks whether it is a leap year or not
Prints Yes or No accordingly

📘 Leap Year Rules (Important)
A year is a leap year if:

It is divisible by 4
Except if it is divisible by 100, then it is not a leap year
Unless it is also divisible by 400, then it is a leap year

➕ Examples:

2000 ✅ (Leap year – divisible by 400)
1900 ❌ (Not a leap year – divisible by 100, but not 400)
2024 ✅ (Leap year – divisible by 4, not 100)
'''

year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


'''
Leap Year with Range Check
✅ Task:
Write a program that:

Takes two years as input: a starting year and an ending year.
Prints all leap years in that range (inclusive).
Makes sure to validate the inputs — starting year should not be greater than the ending year.
Uses the correct leap year logic:

A year is a leap year if:

Divisible by 4, and
Not divisible by 100 unless also divisible by 400
'''

start_year = int(input("Enter starting year:"))
end_year = int(input("Enter ending year:"))

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}")