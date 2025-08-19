'''
Mini Mission 4: Dictionary Key Finder

Badge Progress: 🧩 Working toward Dictionary Dynamo

🧪 Mission Brief:
You're given a predefined dictionary of products and prices.
Your job is to let the user search for a key and tell them whether it exists and, if it does, show its value.

🧾 Requirements:
Prompt the user to enter a product name (case-insensitive).

Check if that key exists in the dictionary.

If found:

✅ Print the product and its price.

If not found:

❌ Show a “Product not found” message.

Allow the user to search again or exit.
'''
def dict_key_finder(dict):
    while True:
        input_string = input("Enter product to search: ").lower().strip().split()
        for item in input_string:
            if item in dict:
                print(f"✅ {item} is available at ₹{dict[item]}")
            else:
                print(f"❌ {item} is not available.")
        choice = input("Search again? (yes/no): ").lower().strip()
        if choice == "yes":
            continue
        elif choice == "no":
            return "Exiting the product finder."
dict = {
    "apple": 30,
    "banana": 10,
    "chocolate": 50,
    "milk": 25,
    "bread": 20
}

result = dict_key_finder(dict)
print(result)