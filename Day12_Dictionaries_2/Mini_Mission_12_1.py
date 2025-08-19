'''
🎯 Day 12 - Mini Mission 1: Inventory Stock Manager
📁 Filename: inventory_stock.py
🧠 Concepts used: Nested dictionaries, value updates, .get() for safe access

🛒 Mission Brief:
You are managing a small store. The inventory has categories, and each category has items with quantity and price stored inside. Your job is to:

Show the current stock (nicely formatted).

Let the user:

Update quantity or price of an item
Add a new item under a category
Create a new category if it doesn’t exist
Show the updated stock after every action.
Repeat until the user exits.
'''

def inventory_stock_manager(inventory):
    print("Current Inventory: ")
    for category in inventory:
        print(f"\nCategory: {category.title()}")
        for item, details in inventory[category].items():
            quantity = details["quantity"]
            price = details["price"]
            print(f" {item.title()} - Qty: {quantity}, Price: ₹{price}")

def update_item(inventory):
    category = input("Enter category name: ").lower().strip()
    if category in inventory:
        item = input("Enter item name: ").lower().strip()
        if item in inventory[category]:
            details = inventory[category][item]
            print(f"Current Qty: {details['quantity']}, Price: ₹{details['price']}")
            new_quant = int(input("Enter new quantity: "))
            new_price = int(input("Enter new price: "))
            details["quantity"] = new_quant
            details["price"] = new_price
            print(f"✅{item.title()} added successfully.")
        else:
            print("❌ Item not found.")
    else:
        print("❌ Category not found.")

def add_new_item(inventory):
    choice = input("Do you want to add a new category?(Yes/No): ").lower().strip()
    if choice == "yes":
        new_category = input("Enter new category name: ").lower().strip()
        inventory[new_category] = {}
    elif choice == "no":
         new_category = input("Enter existing category name: ").lower().strip()
         if new_category not in inventory:
             print("❌ Category does not exist.")
             return
    item = input("Enter new item name: ").lower().strip()
    quantity = int(input("Enter quantity: "))
    price = int(input("Enter price: "))
    inventory[new_category][item] = {"quantity": quantity, "price": price}
    print(f"🆕 {item.title()} added to {new_category.title()}.")

def ism_menu(inventory):
    while True:
        print("\nWhat would you like to do? ")
        print("1. Update item")
        print("2. Add new item")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            update_item(inventory)
        elif choice == "2":
            add_new_item(inventory)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

inventory = {
    "fruits": {
        "apple": {"quantity": 10, "price": 30},
        "banana": {"quantity": 20, "price": 10}
    },
    "diary": {
        "milk": {"quantity": 15, "price": 25}
    }
}

inventory_stock_manager(inventory)
ism_menu(inventory)