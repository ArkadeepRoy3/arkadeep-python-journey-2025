'''
🛠️ Mini Mission 5: Dictionary Updater
Objective:
Write a program that updates the price of an item in a dictionary or adds it if it doesn't exist.
✅ Your Task
Write a function like this:

def update_price(store):
    # ask user for product name and new price
    # if product exists, update price
    # if not, add it as new entry
    # print confirmation message

🎯 Example:

Enter product name: chocolate
Enter new price: 60
✅ Price of chocolate updated to ₹60

Enter product name: eggs
Enter new price: 12
🆕 Added new product: eggs at ₹12

Ask the user if they want to update another product (loop) and finally display the full updated dictionary.
'''

def update_price(store):
    while True:
        print(f"Inventory: ")
        for key, value in store.items():
            print(f"Item: {key} => Price: ₹{value}")
        product_name = input("Enter product name: ").lower().strip().split()
        new_price = int(input("Enter new price: "))
        for item in product_name:
            if item in store:
                store[item] = new_price
                print(f"✅ Price of {item} updated to ₹{store[item]}")
            else:
                store[item] = new_price
                print(f"🆕 Added new product: {item} at ₹{new_price}")
                continue
        choice = input("Do you want to continue? (Yes or No): ").lower().strip()
        if choice == "yes":
            continue
        elif choice == "no":
            return
store = {
    "egg": 12,
    "chocolate": 20
}

update_price(store)