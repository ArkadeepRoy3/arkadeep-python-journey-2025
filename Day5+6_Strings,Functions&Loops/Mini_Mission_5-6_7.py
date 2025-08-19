'''
🧪 Mini Mission 7: Leap Year Checker
🗓️ Topic: Conditionals + Functions

🛠️ Your Tasks:

Ask the user to input a year (as an integer)
Write a function is_leap_year(year) that:
Returns True if it's a leap year
Returns False otherwise
Print a user-friendly message based on the result
(e.g., “Yes! 2024 is a leap year.” or “Nope, 2023 is not a leap year.”)
'''

def is_leap_year():
    year = int(input("Please enter the year: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return f"Yes! {year} is a leap year."
    else:
        return f"No! {year} is not a leap year."
    
result = is_leap_year()
print(result)