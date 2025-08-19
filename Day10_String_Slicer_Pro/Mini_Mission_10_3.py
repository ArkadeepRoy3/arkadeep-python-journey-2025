'''
🟩 Mini Mission 3: Tuple Pair Extractor

🎯 Objective:
From a tuple of numbers, extract all pairs of consecutive elements and print them as 2-element tuples.

🧠 Input:
A tuple of integers (entered comma-separated)

🧪 Example:

Enter numbers: 10, 20, 30, 40

Output:
(10, 20)  
(20, 30)  
(30, 40)
💡 Tips:
Use a for loop with index (range)

Remember: tuple[i] and tuple[i+1]

Stop at len(tuple) - 1 to avoid IndexError
'''
numbers = tuple(int(x.strip()) for x in input("Enter numbers: ").strip().split(","))
tuple_list = []
for i in range(len(numbers)-1):
    pair = (numbers[i], numbers[i+1])
    tuple_list.append(pair)
print(tuple_list)