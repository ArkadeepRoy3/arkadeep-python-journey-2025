'''
✅ Mini Mission 7: Even-Odd Sorter
🎯 Goal:
Write a program that asks the user for numbers, stores them in a list, and then separates them into two lists:

One for even numbers
One for odd numbers
'''

original_list = []
even_list = []
odd_list = []

numbers = int(input("Please choose how many numbers do you want to enter: "))

for i in range(numbers):
    number = int(input(f"Enter Number {i+1}: "))
    original_list.append(number)

for item in original_list:
    if item % 2 == 0:
        even_list.append(item)
    else:
        odd_list.append(item)

print(f"Orignial List is: ")
for i in range(len(original_list)):
    print(original_list[i])
    
print(f"Even List is: ")
for i in range(len(even_list)):
    print(even_list[i])

print(f"Odd List is: ")
for i in range(len(odd_list)):
    print(odd_list[i])