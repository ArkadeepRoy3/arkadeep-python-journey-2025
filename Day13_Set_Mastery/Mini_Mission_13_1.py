'''
🧭 Mini Mission 1: Set Explorer
🎯 Goal:
Build a small program that lets users:

Add items to a set
Remove items from the set
View the current set
Exit the program

🛠 Features:
Prompt the user to enter commands like:

add <item>
remove <item>
view
exit

Handle:
Unknown commands
Trying to remove something not in the set (use .discard()!)

🔧 Set Explorer 🔧
Enter a command: add banana
✅ Added banana

Enter a command: add mango
✅ Added mango

Enter a command: view
Current Set: {'banana', 'mango'}

Enter a command: remove banana
🗑️ Removed banana

Enter a command: view
Current Set: {'mango'}

Enter a command: exit
👋 Goodbye!
'''

def se_add(initial_set):
    input_choice = input("Enter item to set: ").lower().strip()
    initial_set.add(input_choice)
    print(f"✅ Added {input_choice}")

def se_remove(initial_set):
    input_choice = input("Enter item to remove from set: ").lower().strip()
    if input_choice in initial_set:
        initial_set.remove(input_choice)
        print(f"✅ Removed {input_choice}")
    else:
        initial_set.discard(input_choice)
        print(f"{input_choice} is not available.")

def se_view(initial_set):
    for item in initial_set:
        print(item.title())

def se_menu(initial_set):
     print("🔧 Set Explorer 🔧")
     while True:
        print("Choose a command")
        print("1. Add item")
        print("2. Remove item")
        print("3. View set")
        print("4. Exit")
        choice = input("Enter a choice: ").lower().strip()

        if choice == "1":
            se_add(initial_set)
        elif choice == "2":
            se_remove(initial_set)
        elif choice == "3":
            se_view(initial_set)
        elif choice == "4":
            return
        else:
            print("Please choose a valid option from the menu.")

initial_set = set()

se_menu(initial_set)