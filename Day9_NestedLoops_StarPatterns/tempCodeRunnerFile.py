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
        print(print_triangle(n))
    elif input_choice == 2:
        print(print_reverse_triangle(n))
    elif input_choice == 3:
        print(print_number_blocks(n))
    else:
        print("Invalid choice. Please select 1, 2 or 3.")

menu()