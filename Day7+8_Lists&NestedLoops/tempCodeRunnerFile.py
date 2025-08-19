'''
🧾 Mini Mission: Matrix Printer
🎯 Objective:
Print a 2D list (matrix) in a clean, formatted matrix style using nested loops.

🧩 Description:
Given a predefined matrix (2D list), loop through it row by row and print the elements in matrix form.

✅ Starter Matrix (you can use this or create your own):

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''

def matrix_printer():
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    print("Matrix:")

    print("Col: ", end="")
    for col_num in range(len(matrix[0])):
        print(f"{col_num:^6}", end="")
    print()

    print("        "+"-"*(len(matrix[0])* 6))

    for i, row in enumerate(matrix):
        print(f"Row {i}: ", end="")
        for val in row:
            print(f"{val:^6}", end="")
        print()

matrix_printer()