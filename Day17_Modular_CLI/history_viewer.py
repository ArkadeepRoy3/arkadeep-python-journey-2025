'''
MM4 - Calculation History Viewer CLI.

Goal:
Build a CLI program that lets users view the calculation logs saved by your previous MM3 logging feature (calc_log.txt or whichever file you used).

What MM4 should do:

Show a menu:
View all logs
Search logs by operation (like +, -, *, /)
Exit
When viewing logs, read and display all entries from the log file.
When searching, filter the entries and show only those matching the operation symbol.
Handle the case when the log file does not exist or is empty.

Here's a step-by-step plan for MM4:

Create a Python module (e.g., history_viewer.py) for this CLI.
Write a function to read the entire log file and print all entries.
Write a function to filter and print entries matching a specific operation.
Make a CLI loop with the menu and handle user inputs accordingly.
Add graceful error handling for file-related issues.
'''
def main(filename):
    while True:
        print("1. View all logs")
        print("2. Search logs by operation (+, -, *, /)")
        print("3. Exit")
        choice = input("Choose an option number: ").strip().replace(".","")

        if choice == "1":
            view_all_logs(filename)
        elif choice == "2":
            search_logs_by_operation(filename)
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid option number from the menu. Try again!")
        

def view_all_logs(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No logs found yet.")
                return
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

def search_logs_by_operation(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            operator = input("Enter the operator: ").strip()
            found = False
            for line in lines:
                if f" {operator} " in line:
                    print(line.strip())
                    found = True
            if not found:
                print("No log found.")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main(filename="calc_log.txt")