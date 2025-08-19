'''
MM3 - Square Mapper
Task: Write a program that takes a list of integers and uses lambda + map() to return a new list containing the square of each number.

Bonus Twist:
Also return a second list containing the cube of each number using the same input list.

Example:

Input:  1, 2, 3, 4  
Output:  
Squares: [1, 4, 9, 16]  
Cubes:   [1, 8, 27, 64]
'''
integer_list = list(map(lambda x: int(x.strip()), input("Enter numbers separated by comma: ").split(",")))
print(f"Original List: {integer_list}")

sqr_list = list(map(lambda x: x**2, integer_list))
cube_list = list(map(lambda x: x**3, integer_list))

print(f"Squares: {sqr_list}")
print(f"Cubes: {cube_list}")