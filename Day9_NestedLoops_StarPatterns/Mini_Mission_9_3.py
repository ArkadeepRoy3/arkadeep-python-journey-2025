'''
🟨 Mini Mission 8: Unique Sorter
Goal: Write a program that takes a list of integers, removes duplicates, sorts the list in ascending order, and prints the result.

🔹 Input Example:

Enter numbers (comma-separated): 4, 2, 5, 2, 3, 4, 1
🔹 Output:

Sorted Unique List: [1, 2, 3, 4, 5]
🔹 Requirements:
Use functions

Make sure the input handles spaces (like "4, 2, 5" correctly)
Do not use set() to remove duplicates — use a manual approach.
'''
def unique_sorter():
    raw_list = list(input("Enter numbers (comma-separated): ").strip().split(","))
    normal_list = []
    final_list = []
    for item in raw_list:
        new = int(item.strip())
        normal_list.append(new)
    normal_list.sort()
    for item in normal_list:
        if item not in final_list:
            final_list.append(item)
    return final_list

result = unique_sorter()
print(result)