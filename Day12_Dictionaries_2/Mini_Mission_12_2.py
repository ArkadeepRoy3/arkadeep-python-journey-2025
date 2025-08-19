'''
🧩 Mini Mission 2: Dict Transformer

🔧 Problem:
You're given a dictionary containing product names and their prices. Your job is to apply a discount to each item and generate a new dictionary with the discounted prices.

📝 Input Example:

products = {
    "laptop": 60000,
    "headphones": 3000,
    "keyboard": 1500,
    "mouse": 700,
}
🎯 Task:

Ask the user to enter a discount percentage (e.g. 10 for 10%).
Create a new dictionary with the same product names but discounted prices.
Round prices to the nearest integer.
Print the original and the discounted price for each product in a clean format.

✅ Example Output:
If the user enters 10, your program might print:

Discount: 10%
Laptop: ₹60000 → ₹54000
Headphones: ₹3000 → ₹2700
Keyboard: ₹1500 → ₹1350
Mouse: ₹700 → ₹630

Try making a function called apply_discount(products, percent) that returns the new dictionary. Use it in your final program.
'''

def apply_discount(products):
    discounted_products = {}
    percent = int(input("Enter the discount percentage: "))
    print(f"Dicount: {percent}%")

    for items in products:
        original_price = products[items]
        discount = original_price * percent/100
        new_price = int(original_price - discount)
        discounted_products[items] = new_price
        print(f"{items.title()}: ₹{original_price} -> ₹{new_price}")

products = {
    "laptop": 60000,
    "headphones": 3000,
    "keyboard": 1500,
    "mouse": 700,
}

apply_discount(products)