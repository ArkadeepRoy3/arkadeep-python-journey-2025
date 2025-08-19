'''
🔐 Mini Mission 5: Loop Password Lock
🎯 Goal:
You will create a password-protected system that:

Asks the user to enter a secret password.
Gives them only 3 attempts to get it right.
If they succeed, print ✅ "Access Granted".
If they fail 3 times, print 🔒 "System Locked".

🧠 Pyro's Notes: while + control flow
You'll need a while loop to keep asking until:

Password is correct ✅
Or 3 wrong attempts ❌
You will need a counter like attempts = 0 and increase it after each wrong try.

💡 Constraints:
Correct password = "python123" (you can hardcode this)
Case-sensitive is fine.
'''
attempt = 0
base_password = "4321"

while attempt < 3:
    secret_password = input("Please enter the password:")
    if base_password == secret_password:
        print("Access Granted ✅")
        break
    else:
        print(f"Access Denied! Try again! Attempts Left: {2-attempt}")
        attempt += 1

if attempt == 3:
    print("Too many attempts! System Locked 🔒.")