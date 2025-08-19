'''
🧪 Mini Mission 9 – List Analyzer
📌 Goal:
Take a list of numbers from the user and analyze the data with useful statistics.

🎯 Your Mission:
Take N numbers as input and then display:

✅ The original list
✅ The total number of elements
✅ The sum of all elements
✅ The average (mean) of the list
✅ The maximum and minimum value in the list
'''

original_list = []
total = 0

numbers = int(input("How many numbers would you like to enter?: "))

for i in range(numbers):
    number = int(input(f"Please enter number {i+1}: "))
    original_list.append(number)

print("📦 Original List: ")
for word in original_list:
    print(f"- {word}")

print(f"🔢 Total Elements: {len(original_list)}")

for i in range(numbers):
    total += original_list[i]

print(f"➕ Sum: {total}")

print(f"📊 Average: {int(total/len(original_list))}")

print(f"⬆️ Max Value: {max(original_list)}")

print(f"⬇️ Min Value: {min(original_list)}")