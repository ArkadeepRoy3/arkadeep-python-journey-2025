'''
🧩 Mini Mission 1: Add Contact System

🎯 Objective:
Build the "Add Contact" feature for the phonebook.

🧠 Input:
Name of the contact (string)

Phone number (string or numeric)

📌 Example:

Enter contact name: Alice  
Enter phone number: 9876543210 

✅ Output:
Store this in a dictionary like:
{"Alice": "9876543210"}

Print: "Contact added successfully!"
'''

def add_contact(phonebook):
    name = input("Enter contact name: ").title().strip()
    if name in phonebook:
        print("❌ Contact already exists!")
        return
    phone = input("Enter phone number: ").strip()
    if not phone.isdigit() or len(phone) != 10:
        print("❌ Invalid phone number. Must be exactly 10 digits.")
        return
    phonebook[name] = phone
    print("Contact added successfully!")

def search_contact(phonebook):        
    choice_name = input("Enter a name to search: ").lower().strip()
    if choice_name in phonebook:
        print(f"Name: {choice_name}")
        print(f"Phone: {phonebook[choice_name]}")
    elif choice_name not in phonebook:
        print("Contact not found.")
    
def view_contacts(phonebook):
    print("\n📇 Final Phonebook:")
    for name, phone in phonebook.items():
        print(f"{name} : {phone}\n")
                
def menu_func():
    while True:
        print("Choose an option:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            view_contacts(contacts)
        elif choice == "4":
            return "Have a nice day!"

contacts = {}

menu_func()