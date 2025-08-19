'''
🧭 Mini Mission 10 – List Searcher
🎯 Goal:
Create a program that asks the user to input a list of items and then search for a specific item in that list.

✅ Your Task:
Ask how many items the user wants to enter.

Take input for each item (e.g., strings like names, items, etc.).
Store all inputs in a list.
Ask the user to enter a word/item to search.

Check:

If the item exists → print ✅ Item found at index: <position>.
If not → print ❌ Item not found in the list.
'''

original_list = []

number = int(input("How many items would you like to enter?: "))

for i in range(number):
    item = input(f"Enter the item {i+1}: ")
    original_list.append(item)

search_item = input("Which item would you like to search?: ").lower()

found = False

for i in range(number):
    if original_list[i].lower() == search_item:
        print(f"✅ Item found at index: {i+1}")
        found = True
        break

if not found:
    print("❌ Item not found in the list.")