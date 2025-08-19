'''
🧩 Combo Mission: String Surgeon Challenge
🪄 Focus: .replace(), .split(), .join(), .strip(), .title()
🎯 Wrap up Mini Missions 5 & 6 in one go

✅ Your Task:
Write a program that:

Asks the user to enter a messy sentence:

May contain unwanted spaces
May use a placeholder word like "Python" multiple times

The program should:

Strip leading/trailing spaces
Replace every "Python" with "String World"
Count how many words the cleaned sentence contains

Convert the cleaned sentence to:

Uppercase
Title Case
Show all outputs cleanly

🖼️ Sample Output:

Enter a sentence:   I love Python. Python is powerful.   

✅ Cleaned sentence: I love String World. String World is powerful.
✅ Word count: 7
✅ Uppercase version: I LOVE STRING WORLD. STRING WORLD IS POWERFUL.
✅ Title case version: I Love String World. String World Is Powerful.
'''

def string_surgeon():
    input_sentence = input("Enter a sentece: ").strip()
    cleaned_sentence = input_sentence.replace("Python", "String World")
    print(f"✅ Cleaned sentence: {cleaned_sentence}")
    word_list = input_sentence.split()
    print(f"✅ Word count: {len(word_list)}")
    print(f"✅ Uppercase version: {cleaned_sentence.upper()}")
    print(f"✅ Title case version: {cleaned_sentence.title()}")

string_surgeon()