'''
🧩 Mini Mission 2: Star Pattern Printer
📌 Task:
Write a program that takes an integer input n from the user and prints a right-angled triangle pattern of stars * using nested loops like this:

Input: 5

*
* *
* * *
* * * *
* * * * *
🔧 Constraints:

Use nested for loops only.

No string multiplication ('*' * i) — use loops to print each star.
'''

def star_pattern():
    number = int(input("Input: "))
    for rows in range(1, number+1):
        for item in range(rows):
            print("*", end=" ")
        print()
        
star_pattern()