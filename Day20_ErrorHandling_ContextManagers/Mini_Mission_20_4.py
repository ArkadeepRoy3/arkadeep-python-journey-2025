'''
📜 Challenge: Double Writer

You are tasked with creating a small logging utility that writes into two different files at the same time.

Requirements:

Use nested context managers (with) to open two files simultaneously (file1.txt and file2.txt).

Write the message "Double write successful!" into both files.

Ensure the files are closed automatically after writing (no explicit .close()).

After writing, open both files again (safely) and print their contents to verify the result.

Hint: Think of this as "broadcast writing" — one action should update multiple files.
'''
try:
    with open("file1.txt", 'w+') as f1, open("file2.txt", 'w+') as f2:
            for f in (f1, f2):
                 f.write("Double write successful!")
            
            for f in f1, f2:
                 f.seek(0)
                 print(f.read())
except FileNotFoundError as e:
    print(f"Error: {e}")