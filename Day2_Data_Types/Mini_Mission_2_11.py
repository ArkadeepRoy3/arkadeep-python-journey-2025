'''
Temperature Converter
🎯 Goal:
Convert temperature from Celsius to Fahrenheit and vice versa based on user input.

📥 Input from user:

A temperature value (can be a float).
A choice of conversion: "C to F" or "F to C".

📤 Output:

If user chose "C to F": convert using F = (C * 9/5) + 32
If user chose "F to C": convert using C = (F - 32) * 5/9
Also, round the result to 2 decimal places and print a clear output.
'''

temp = float(input("Please enter the temperature:"))

choice = input("Enter conversion type (C to F / F to C):")

clean_choice = choice.replace(" ","")

if clean_choice.lower() == "ctof":
    F = (temp * 9/5) + 32
    print(f"{temp}°C is {F:.2f}°F")
elif clean_choice.lower() == "ftoc":
    C = (temp - 32) * 5/9
    print(f"{temp}°F is {C:.2f}°C")
else:
    print("Please choose the correct option! (Either 'C to F' or 'F to C')")