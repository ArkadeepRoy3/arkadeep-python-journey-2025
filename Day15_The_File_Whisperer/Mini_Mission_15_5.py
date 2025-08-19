'''
📜 Mini Mission 5: Simple File CLI Tool
🎯 Goal:

Create a command-line interface where the user can enter commands like:
read <filename> → prints the contents of the file
lines <filename> → prints the number of lines in the file
append <filename> → asks the user to type a new line and adds it to the file
exit → quits the program

🛠️ Key Concepts:

Use input() to continuously take user commands
Use .split() to break the command into parts
Use basic file modes:

'r' → read
'a' → append
Handle invalid input or missing filenames

🚦CLI Command Flow - Example:

> read notes.txt
[prints contents]

> lines notes.txt
Total lines: 12

> append notes.txt
Type a line to add: Python is powerful
Line added!

> read notes.txt
[updated content]

> exit
Goodbye!

⚠️ Edge Cases to Handle:

No filename provided (e.g., read)
File doesn't exist
Invalid command
'''
import string

def read_file(filename):
    try:
        with open(filename.strip(), 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("No file found with that name.")

def count_lines(filename):
    count = 0
    try:
        with open(filename.strip(), 'r') as file:
            for line in file:
                count += 1
        print(f"Total lines: {count}")
    except FileNotFoundError:
        print("No file found with that name.")

def append_lines(filename):
    try:
        with open(filename.strip(), 'a') as updated_file:
            content = input("Type a line to add: ").strip()
            if content:
                updated_file.write(content + '\n')
                print("Line added.")
            else:
                print("No content entered.")
    except FileNotFoundError:
        print("No file found with that name.")

def read_updated_file(filename):
    read_file(filename)

def file_cli_menu():
    while True:
        print("--- Simple File CLI Tool ---")
        print("1. Read file")
        print("2. Count total lines")
        print("3. Add a line to file")
        print("4. Read updated file")
        print("5. Exit")
        choice = input("Please enter the choice number: ").strip()
        choice = choice.translate(str.maketrans('','', string.punctuation))
        if choice == "1":
            filename = input("> read: ").strip()
            read_file(filename)
        elif choice == "2":
            filename = input("> lines: ").strip()
            count_lines(filename)
        elif choice == "3":
            filename = input("> append: ").strip()
            append_lines(filename)
        elif choice == "4":
            filename = input("> read: ").strip()
            read_updated_file(filename)
        elif choice == "5":
            print("Goodbye!")
            return
        else:
            print("Please enter the correct choice from the menu.")

file_cli_menu()