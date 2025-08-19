'''
🧩 Mini Mission 1: Magic Mirror
🔹 Focus: String reversal + case transformations
📦 Skills used: Indexing, slicing, .upper(), .lower(), .title()

🎯 Your Task:
Write a Python program that:

Takes a string input from the user
Reverses the string
Converts the reversed string to:
Uppercase
Lowercase
Title Case
Prints all 3 transformed versions, clearly labeled

🖼️ Example

Enter a string:  PyThon Rocks

Reversed: skcoR nohTyP
Uppercase: SKCOR NOHTYP
Lowercase: skcor nohtyp
Title Case: Skcor Nohtyp
'''
def magic_mirror():
    input_string = input("Enter a sentence/word: ").lower().strip()
    reverse_string = input_string[::-1]
    uppercase_string = reverse_string.upper()
    lowercase_string = reverse_string.lower()
    title_string = reverse_string.title()
    print(f"Reversed: {reverse_string}")
    print(f"Uppercase: {uppercase_string}")
    print(f"Lowercase: {lowercase_string}")
    print(f"Title case: {title_string}")

magic_mirror()