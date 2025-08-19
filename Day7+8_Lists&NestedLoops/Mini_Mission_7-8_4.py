'''
🧪 Mini Mission: Pattern Printer
🎯 Mission Objective:
Print fun and structured patterns using nested loops.

✅ Your Tasks:
Print a Right-Angled Triangle of Stars:

*
* *
* * *
* * * *
* * * * *

Print a Right-Angled Triangle of Numbers:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Print an Inverted Star Triangle:

* * * * *
* * * *
* * *
* *
*
'''

def pattern_printer():
    rows = int(input("Enter the number of rows: "))
    choice = input("Choose the option that you want to print (Pattern/Number): ").lower()

    if choice == "pattern":
        pattern = input("Enter the pattern you want to print: ")
        order = input("Do you want to print pattern in normal or reverse: ").lower()
        if order == "normal":
            for i in range(1, rows+1):
                print((pattern + " ")*i)
        else:
            for i in range(rows, 0 , -1):
                print((pattern + " ")*i)
    elif choice == "number":
        order = input("Do you want to print pattern in normal or reverse: ").lower()
        if order == "normal":
            for i in range(1, rows+1):
                for j in range(1, i+1):
                    print(j, end=" ")
                print()
        else:
            for i in range(rows, 0, -1):
                for j in range(1, i+1):
                    print(j, end=" ")
                print()
    else:
        print("Invalid choice. Please select either 'pattern' or 'number'.")
        
pattern_printer()