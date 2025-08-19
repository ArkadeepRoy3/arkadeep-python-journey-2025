'''
🟨 Mini Mission 8: Number Blocks + Pattern Menu
📄 Filename: pattern_menu_with_functions.py

Part A: Basic Number Block
For input n = 3, print:

1 2 3
1 2 3
1 2 3
Part B: Add Menu

1. Star Triangle
2. Reverse Triangle
3. Number Block
User selects from the menu, and appropriate pattern is printed.

💡 Bonus: Modularize with functions

def print_triangle(n):

def print_reverse_triangle(n):

def print_number_block(n):
'''

def print_triangle(n):
    for rows in range(1, n+1):
        for element in range(rows):
            print("*", end=" ")
        print()

def print_reverse_triangle(n):
    for rows in range(n, 0, -1):
        for element in range(rows):
            print("*", end=" ")
        print()

def print_number_blocks(n):
    for rows in range(1, n+1):
        for num in range(1, n+1):
            print(num, end=" ")
        print()

def menu():
    print("1. Star Triangle")
    print("2. Reverse Triangle")
    print("3. Number Block")
    input_choice = int(input("Please choose an option from the menu: "))
    n = int(input("Enter the value of n: "))
    if input_choice == 1:
        print_triangle(n)
    elif input_choice == 2:
        print_reverse_triangle(n)
    elif input_choice == 3:
        print_number_blocks(n)
    else:
        print("Invalid choice. Please select 1, 2 or 3.")

menu()