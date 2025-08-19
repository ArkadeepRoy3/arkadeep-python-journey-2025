# My road to becoming a Python developer - Arkadeep Roy - 01.07.2025
print("Hello World! I am starting my journey to becoming a python developer.")

name = input("What is your name?")
print("Nice to meet you",name)

age = input("Enter your age:")
age = int(age)
print("You'll be", age + 1,"next year!")

birth_year = int(input("Enter your birth year:"))
current_year = 2025
print("You are", current_year - birth_year,"years old.")

#Basic Math 

a = 12
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

#Type Checking

x = 7
y = "Arka"
z = 3.14

print(type(x))
print(type(y))
print(type(z))

#String Formatting - Best Practice!

name = "Arkadeep"
age = 26

print(f"My name is {name} and I am {age} years old!") # f-string

#String Manipulation

message = "  Hello Arka!  "

print("Original:", message)
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Stripped:", message.strip())
print("Replaced:", message.replace("Arka", "Hero"))
print("Length:", len(message))

#Indexing and Slicing

word = "Python"
print(word[0])
print(word[-1])
print(word[1:4])