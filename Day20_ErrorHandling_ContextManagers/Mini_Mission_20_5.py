'''
MM5: Error Inside Manager.

Challenge Statement:

Write a program that:

Opens a file using a context manager (with open(...)).
Inside the block, try performing an operation that may fail (e.g., dividing by zero, or converting a string to int).
Catch the error properly while still inside the with block.
Make sure the file closes safely even when an error occurs.
👉 The goal: Show that context managers + error handling play nicely together.
'''
try:
    with open("sample.txt", 'w+') as file:
        file.write("Hi!")
        file.seek(0)
        print(file.read())

        try:
            result = 10 / 0
            print(result)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
except FileNotFoundError as e:
    print(f"Error {e}")