'''
Smart Access Control (v2)
🎯 Goal:
Build a smart access control system that decides whether a person can enter based on age, valid ID, and secret code.

✅ You will need:
Nested if statements
Compound conditions
Input normalization (like lower() for Yes/No)
Age check (18 and above allowed)
Valid ID (must be 'yes')
Secret code (must be 'yes')
'''

age = int(input("Please enter your age:"))
id = input("Do you have a valid ID? Yes/No:")
secret_code = input("Do you have the secret code? Yes/No:")

id = id.strip().lower()
secret_code = secret_code.strip().lower()

if age >= 18:
    if id == "yes":
        if secret_code == "yes":
            print("Access Granted!")
        else:
            print("You must have the secrert code!")
    else:
        print("You should have a valid id!")
else:
    print("You must be 18 years or older!")