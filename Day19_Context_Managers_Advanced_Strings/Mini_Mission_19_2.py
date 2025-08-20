'''
📝 MM2 - Line Counter

Task:
Create a text file called lines.txt.
Write at least 3-4 lines of text into it (each on a new line).
Reopen the file with a context manager.
Count how many lines are inside and print the result.
'''
with open("lines.txt", 'w') as file:
    file.writelines(["Python is fun\n","Context managers are useful\n", "Files are easy with with\n"])

with open("lines.txt", 'r') as file:
    print(file.read())    

with open("lines.txt", 'r') as file:
    count = sum(1 for _ in file)
    print(f"Total lines: {count}")