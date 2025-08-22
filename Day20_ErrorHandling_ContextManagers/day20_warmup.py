'''
🔥 Warm-up Tasks

Zero Division Guard
Write a small function that divides two numbers but gracefully handles ZeroDivisionError and prints "Division by zero not allowed!".

File Reader with Fallback
Try to open a file "day20.txt".

If it exists, print its contents.

If it doesn't, catch the FileNotFoundError and instead print "File missing! Creating it...", then create the file with some starter text.

Safe Int Conversion
Take a list like ["10", "20", "hello", "30"].

Convert each element to an integer.

If conversion fails, catch the ValueError and skip that element.

Print the cleaned integer list.
'''
#1

def zero_division_guard(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero. {e} error.")

print(zero_division_guard(6,0))

#2

try:
    with open("day20.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File missing! Creating it....")
    with open("day20.txt", 'w') as file:
        file.write("Created this file because it was not created earlier. Bye bye.")

#3

input_list = ["10", "20", "hello", "30"]
new_list = []

for item in input_list:
    try:    
        new_list.append(int(item))
    except ValueError:
        print(f"Cannot convert '{item}' to integer. Skipping.")

print(new_list)