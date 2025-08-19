'''
🧪 Practice Task 1: File Pointer Basics

Open a file called sample.txt in read mode.
Read only the first 10 characters.
Then use seek() to reset the pointer to the start.
Print the full file content.
🧠 Practice how read() and seek() work.
'''
def practice_read_seek():
    filename = input("Enter the filename: ").strip()
    if not filename.endswith(".txt"):
        raise ValueError("Only .txt file allowed")
    try:
        with open(filename, 'r') as file:
            print(file.read(10))
            file.seek(0)
            print(file.read())
    except FileNotFoundError:
        print("File was not found.")
    
practice_read_seek()

'''
🧪 Practice Task 2: Write vs Append Modes

Open a file called testfile.txt
First, use mode 'w' to write: "First line"
Then, open it again in 'a' mode and add: "Second line"
Finally, read and print the entire content.
🧠 Understand how w overwrites, and a appends.
'''

def w_and_a():
    filename = input("Enter the filename: ").strip()
    if not filename.endswith(".txt"):
        raise ValueError("Only .txt file allowed")
    try:
        with open(filename, 'w') as file:
            file.write("First line" + '\n')
        with open(filename, 'a') as file:
            file.write("Second line")
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")

w_and_a()

'''
🧪 Practice Task 3: try + else + finally

Ask the user to enter a filename
Try to open and read it
If the file doesn't exist, handle the error
If it succeeds, print “Read successful!” in the else block
Always print “End of operation” in finally
🧠 Helps reinforce structured exception handling
'''
def try_else_finally_prac():
    filename = input("Enter the filename: ").strip()
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt file allowed")
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Read successful!")
    finally:
        print("End of operation.")

try_else_finally_prac()