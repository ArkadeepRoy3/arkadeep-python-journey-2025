'''
MM1 - Quick Math Ops
Goal: Create 4 lambda functions to perform:

Addition
Subtraction
Multiplication
Division

Details:

Use lambda syntax.
Each should take two numbers.
Print example results for each operation.

Example (for addition):

add = lambda a, b: a + b
print(add(5, 3))  # 8
'''
add = lambda a, b: a + b
print(add(5,3))

sub = lambda a, b: a - b
print(sub(5,3))

multiply = lambda a, b: a * b
print(multiply(2,3))

divide = lambda a,b: a / b if b != 0 else "Cannot divide by 0."
print(divide(6,2))