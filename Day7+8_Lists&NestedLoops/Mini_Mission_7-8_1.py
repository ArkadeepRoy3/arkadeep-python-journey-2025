'''
🧪 Mini Mission 1: Grocery Basket 🧺
Title: “List & Let Shop!”
Goal: Create and manage a shopping list using list operations.

🧠 Your Tasks:

📥 Ask the user to add items to their basket using a loop.
➕ Use append() to store them in a list.
❓ Ask if they want to remove any items, then use remove() if yes.
🔁 Show the final list of items using a loop.
'''

def grocery_basket():
    grocery_list = []
    print("Welcome to Grocery Basket Manager!")
    number = int(input("How many items would you like to add?: "))

    for i in range(number):
        item = input(f"Enter item {i+1}: ").lower().strip()
        item = item.title()
        grocery_list.append(item)

    choice = input("Would you like to remove any item? (Yes/No): ").lower()
    if choice == "yes":
        remove_item = input("Enter the item to remove: ").strip().title()
        if remove_item in grocery_list:
            grocery_list.remove(remove_item)
        else:
            print(f"'{remove_item}' is not in your basket.")
        
    print("\n🛒 Final Grocery Basket:")
    for item in grocery_list:
        print(f"- {item}")
        
result = grocery_basket()
print(result)