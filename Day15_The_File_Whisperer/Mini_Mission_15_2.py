'''
✅ Mini Mission 2: Word and Character Stats
🔹 Objective:
Write a program that reads a file and displays:

Total number of words

Total number of characters (excluding newline \n)

🔍 Example
File: sample.txt

Hello Pyro  
Python is amazing  
I love coding

Output:

Words: 7
Characters: 42

📝 Notes:

Words are separated by spaces.
Characters exclude newline characters.
Don't count newline \n in character count.
'''

def word_char_stats():
    filename = input("Enter a filename (use .txt at the end of the filename): ").strip()
    try:
        word_count = 0
        letter_count = 0
        with open(filename, 'r') as file:
            lines = file.readlines()
            for sentence in lines:
                word_list = sentence.split()
                print(word_list)
                for word in word_list:
                    word_count += 1
                    for letter in word:
                        letter_count += 1
            print(f"Total word count: {word_count}")
            print(f"Total character count: {letter_count}")
    except FileNotFoundError:
        print("File is not present")

word_char_stats()

#OR 

def word_char_stats():
    filename = input("Enter a filename (use .txt at the end): ").strip()
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
            word_count = len(content.split())
            char_count = len(content.replace("\n", ""))
            print(f"Words: {word_count}")
            print(f"Characters: {char_count}")
    except FileNotFoundError:
        print("File not found.")

word_char_stats()
