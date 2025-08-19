'''
🧪 Mini Mission 3: Matrix Printer
🎯 Goal:
Print elements of a 2D list (a list of lists) in a structured, grid-like format.

📌 Your Tasks:
✅ Use a predefined 2D list (you can later make it user input if you want)
✅ Loop through each row and then through each element
✅ Print the matrix neatly as rows and columns
✅ Bonus: Try using join() for more elegant printing (if you feel confident)

'''
def print_matrix():
    matrix_list = [[1,2,3],[4,5,6],[7,8,9]]
    print("Matrix:")
    for row in matrix_list:
        for element in row:
            print(element, end="\t")
        print()

print_matrix()