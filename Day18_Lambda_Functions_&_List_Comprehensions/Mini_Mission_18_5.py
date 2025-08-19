'''
MM5 - Common Elements Finder
Task:
Write a program that takes two lists of integers from the user and uses lambda + filter() to find common elements.

The output list should not have duplicates.

The elements should appear in the order they appear in the first list.

Example:

Input list 1: 1, 2, 3, 4, 5  
Input list 2: 4, 5, 6, 7, 8  

Output: [4, 5]
'''
list_a = list(int(x) for x in input("Enter numbers separated by comma: ").strip().split(","))
list_b = list(int(y) for y in input("Enter numbers separated by comma: ").strip().split(","))

output_list = list(dict.fromkeys(filter(lambda x: x in list_b, list_a)))
print(output_list)