'''
🧩 Mini Mission 4: Name Beautifier
🪄 Focus: .strip(), .title(), string cleanup

🎯 Your Task:
Write a program that:

Prompts the user to enter a full name (can be messy or badly formatted).

Cleans it up by:

Removing leading/trailing spaces using .strip()
Converting it to title case using .title()

Prints:

The cleaned-up version of the name

🖼️ Example:

Enter your name:   aRkA roy   
✅ Cleaned Name: Arka Roy
'''

def name_beautifier():
    input_name = input("Enter your name: ").strip()
    cleaned_name = input_name.title()
    print(cleaned_name)

name_beautifier()