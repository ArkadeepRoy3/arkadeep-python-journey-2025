
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