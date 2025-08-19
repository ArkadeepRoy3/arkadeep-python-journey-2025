'''
🟩 Mini Mission 3: Even-Odd Tuple Splitter

🎯 Objective:
Split a tuple of numbers into two separate tuples:

One containing even numbers

One containing odd numbers

🧠 Input:
A tuple of comma-separated integers from the user.

🧪 Example:

Enter numbers: 3, 6, 1, 8, 9, 2
Output:
Even numbers: (6, 8, 2)
Odd numbers: (3, 1, 9)
'''

numbers = tuple(int(x.strip()) for x in input("Enter numbers: ").strip().split(","))
even_tuple = []
odd_tuple = []
for item in numbers:
    if item % 2 == 0:
        even_tuple.append(item)
    else:
        odd_tuple.append(item)
even_tuple = tuple(even_tuple)
odd_tuple = tuple(odd_tuple)
print(f"Even numbers: {even_tuple}")
print(f"Odd numbers: {odd_tuple}")