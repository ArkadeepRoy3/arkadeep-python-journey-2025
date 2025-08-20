'''
Warmup:
🎯 Simple Mission (before MMs)
👉 Create a file called notes.txt

Write this line:

Context Managers are powerful!

Close automatically with with.
Reopen it and print the contents.
'''

with open("notes.txt", 'w') as file:
    file.write("Context Managers are powerful!")

with open("notes.txt", 'r') as file:
    print(file.read())

'''
📝 MM1 - Safe Writer

Task:
Use a context manager (with) to open a file called safe.txt.
Write the text:

Python makes file handling safe!

Reopen the same file (again with with) in read mode.
Print the contents.
'''

content = "Python makes file handling safe!"
with open("safe.txt", 'w') as file:
    file.write(content)

with open("safe.txt", 'r') as file:
    print(file.read())