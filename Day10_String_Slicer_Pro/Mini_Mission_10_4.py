'''
🟩 Mini Mission 4: Tuple Reverser

🧠 Objective:
Reverse a given tuple of integers.

🧪 Example:
Input:

Enter numbers: 1, 3, 5, 7
Output:

Reversed tuple: (7, 5, 3, 1)
'''
numbers = tuple(int(x.strip()) for x in input("Enter numbers: ").strip().split(","))
print(f"Reversed tuple : {numbers[::-1]}")