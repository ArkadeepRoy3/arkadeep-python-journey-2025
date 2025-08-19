'''
🟩 Mini Mission 5: Tuple Swapper

Objective:
Swap the first and last elements of a tuple.

Example:

Input: (10, 20, 30, 40)  
Output: (40, 20, 30, 10)

Bonus Challenge:
Try it for tuples with just 1 element, or even empty tuples.
'''

numbers = tuple(int(x.strip()) for x in input("Input: ").strip().split(","))
tuple_list = list(numbers)
temp_list = [tuple_list[0]]
tuple_list[0] = tuple_list[-1]
tuple_list[-1] = temp_list[0]
tuple_list = tuple(tuple_list)
print(tuple_list)

# OR

numbers = tuple(int(x.strip()) for x in input("Input: ").strip().split(","))

if len(numbers) >= 2:
    tuple_list = list(numbers)
    tuple_list[0], tuple_list[-1] = tuple_list[-1], tuple_list[0]
    numbers = tuple(tuple_list)

print(numbers)