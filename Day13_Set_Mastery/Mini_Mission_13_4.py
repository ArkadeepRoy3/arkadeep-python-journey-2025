'''
🎯 Mini Mission 4: Unique Collector
Objective:
Write a program that accepts a list of items (comma-separated), removes duplicates, and displays the unique items in sorted order.

✅ Your Task:
Prompt the user:

Enter a list of items (comma-separated):
Store only unique items (use a set).
Clean up each item using .strip() and normalize casing (e.g., .title()).
Display them in alphabetical order with a friendly message.

🧪 Sample Run:

Enter a list of items (comma-separated): apple, Banana, apple, mango ,Banana, pear
🧺 Unique items collected:
Apple
Banana
Mango
Pear
'''

def unique_collector():
    list_of_items = input("Enter a list of items (comma-separated): ").lower().strip().split(",")
    unique_set = set()

    for item in list_of_items:
        unique_set.add(item.strip().title())
    
    print("🧺 Unique items collected:")
    for item in sorted(unique_set):
        print(item.strip().title())

unique_collector()