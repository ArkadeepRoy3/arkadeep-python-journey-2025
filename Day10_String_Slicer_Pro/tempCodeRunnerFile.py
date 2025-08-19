'''
🟩 Mini Mission 6: Tuple Combiner

🧠 Objective:
Combine two user-input tuples into one.

📥 Input:
Two tuples of integers (comma-separated)

📤 Output:
A single tuple with elements of both, combined in order.

🧪 Example:

Enter first tuple: 1, 3, 5  
Enter second tuple: 2, 4, 6  

Combined tuple: (1, 3, 5, 2, 4, 6)
'''
first_tuple = tuple(int(x.strip()) for x in input("Enter first tuple: ").strip().split(","))
second_tuple = tuple(int(x.strip()) for x in input("Enter the second tuple: ").strip().split(","))

first_list = list(first_tuple)
second_list = list(second_tuple)
third_list = []
for i in first_list:
        third_list.append(i)
for i in second_list:
        third_list.append(i)
final_list = tuple(third_list)
print(final_list)