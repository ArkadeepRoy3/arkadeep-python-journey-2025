'''
🧩 Mini Mission 3: Login Validator
🔐 Focus: .startswith(), .isalnum(), input validation

🎯 Your Task:
Write a program that:
Prompts the user to enter a username.

Checks if the username is valid based on these rules:

✅ Must start with a letter (a-z or A-Z)
✅ Must contain only alphanumeric characters (letters and numbers — no symbols or spaces)

Print:

✅ "✅ Valid username!" if all rules pass
❌ "❌ Invalid username!" if any rule fails

🖼️ Example:

Enter a username: arka123
✅ Valid username!

Enter a username: 123arka
❌ Invalid username!

Enter a username: arka@dev
❌ Invalid username!
'''

def login_validator():
    user_name = input("Enter a username: ")
    if user_name[0].isalpha() and user_name.isalnum():
        print("✅ Valid username!")
    else:
        print("❌ Invalid username!")

login_validator()