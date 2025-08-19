'''
🧠 Mini Mission 8: Logic Combo Fun
🎯 Concepts Covered:
Logical operators (and, or, not), function returns, clean condition design

💼 Your Task
Write a function that does the following:

📋 Problem Statement:

Ask the user three questions:
Do you have a passport?
Do you have a visa?
Is your passport expired?
Then based on this input, decide if the user is eligible to travel internationally.
'''

def travel_int():
    passport = input("Do you have a passport? Yes/No: ").lower()
    visa = input("Do you have a Visa? Yes/No: ").lower()
    passport_expire = input("Is your passport expired? Yes/No: ").lower()

    if passport == "yes":
        if visa == "yes":
            if passport_expire == "no":
                return "✅ You are eligible to travel internationally!"
            else:
                return "❌ Sorry, you're not eligible to travel internationally."
        else:
                return "❌ Sorry, you're not eligible to travel internationally."
    else:
                return "❌ Sorry, you're not eligible to travel internationally."
    
result = travel_int()
print(result)