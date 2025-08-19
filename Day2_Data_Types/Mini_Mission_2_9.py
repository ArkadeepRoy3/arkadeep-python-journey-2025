'''
Advanced String Formatter

Mission Goal:

You'll write a program that takes user input and then:
Shows the name left-aligned, right-aligned, and center-aligned.

Formats a floating-point number to:

2 decimal places
Currency format (₹)
Scientific notation
Bonus: Format two fields side-by-side using alignment and width control.

Input to Collect:

A name from the user.
A float number (like a salary, price, or weight).
'''

name = input("Enter a name:")
float_number = float(input("Enter a float number:"))

print(f"Name Left Aligned: {name:<10}")
print(f"Name Right Aligned: {name:>10}")
print(f"Name Centre Aligned: {name:^10}")
print(f"Float with 2 decimals: {float_number:.2f}")
print(f"Currency Format (₹): ₹{float_number:,.2f}")
print(f"Scientific Notation: {float_number:e}")

print(f"|Name       |Amount |\n|-----------|-------|")
print(f"|{name:<10} |{float_number:,.2f}|")