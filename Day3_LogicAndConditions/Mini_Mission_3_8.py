'''
🧪 Mini Mission 8: Secure PIN Verification 🔐
🎯 Mission Goals:
Practice user input, string comparison, and logic conditions
Implement a basic authentication system
In this mission, you're creating a simple PIN-based verification system. Here's how it works:

✅ Basic Requirements:
Ask the user to enter a 4-digit PIN.

Compare it with a predefined correct PIN (e.g., "4321").
If it matches: print "Access Granted ✅".
If not: print "Access Denied ❌".

Bonus: Add limited attempts (optional):

Allow the user 3 attempts maximum.
After 3 wrong tries, print "Too many attempts. Access locked 🔒" and stop.
'''

base_pin = 4321
pin = int(input("Enter the 4-digit PIN:"))

if base_pin == pin:
    print("Access Granted ✅")
elif base_pin != pin:
    print("Access Denied ❌")
    pin = int(input("Enter the 4-digit PIN:"))
    if base_pin == pin:
        print("Access Granted ✅")
    elif base_pin != pin:
        print("Access Denied ❌")
        pin = int(input("Enter the 4-digit PIN:"))
        if base_pin == pin:
            print("Access Granted ✅")
        elif base_pin != pin:
            print("Access Denied ❌")
            print("Too many attempts. Access locked 🔒")


# Code using while loop:

base_pin = 4321
attempts = 0

while attempts < 3:
    pin = int(input("Please enter the pin:"))
    if base_pin == pin:
        print("Access Granted ✅")
        break
    else:
        print("Access Denied ❌")
        attempts += 1

if attempts == 3:
    print("Too many attempts. Access locked 🔒")