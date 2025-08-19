'''
The Access Control System
You're building a small entry system for a secure lab. The system checks three conditions before allowing entry:

Age must be 18 or above.
Has a valid ID? (yes or no)
Knows the secret code? (yes or no)

🛠️ Input Requirements:

Ask the user for their age (integer)
Ask Do you have a valid ID? (yes/no)
Ask Do you know the secret code? (yes/no)

✅ Logic for Access:
Entry is granted only if:

Age is 18 or above
AND

Has a valid ID
AND

Knows the secret code
Else, deny access with a proper reason.
'''

age = int(input("Enter your age:"))
id = input("Do you have a valid ID? Yes/No:")
secret_code = input("Do you know the secret code? Yes/No:")

id = id.lower()
secret_code = secret_code.lower()

if age >= 18:
    if id == "yes":
        if secret_code == "yes":
            print("Access granted!")
        else: 
            print("Access Denied: secret code is required.")
    else:
        print("Access Denied: Id is required.")
else:
    print("Access Denied: Must be 18 years or above.")