'''
MM5 - Pointer Explorer 

Write a Python script that:
Shows same-object reference
Create a list, assign it to another variable, and prove both variables point to the same object (use id() to print the memory reference).
Demonstrates mutation effect
Change the second variable's list and prove the first variable sees the change.
Demonstrates immutable behavior
Repeat the same experiment with integers or strings, proving reassignment does not affect the other variable.
Clear Output Format
Clearly label each step in your output so it's easy to follow the logic.

Example Output Flow (just the flow, not exact values)

--- Mutable object test ---
id of list_a: 14012345
id of list_b: 14012345
After modifying list_b: list_a = [...]
--- Immutable object test ---
id of int_a: 14011234
id of int_b: 14011234
After modifying int_b: int_a = ...
'''
def pointer_explorer():
    # Mutable example
    list_a = [1, 2, 3, 4, 5]
    list_b = list_a
    print("\n--- Mutable object test (List) ---")
    print(f"Initially: list_a = {list_a}, list_b = {list_b}")
    print(f"id(list_a) = {id(list_a)}, id(list_b) = {id(list_b)}")
    list_b[0] = 0
    print(f"After modifying list_b: list_a = {list_a}, list_b = {list_b}")
    print("(Both variables point to the same list in memory)\n")

    # Immutable example
    int_x = 5
    int_y = int_x
    print("--- Immutable object test (Integer) ---")
    print(f"Initially: int_x = {int_x}, int_y = {int_y}")
    print(f"id(int_x) = {id(int_x)}, id(int_y) = {id(int_y)}")
    int_y += 10
    print(f"After modifying int_y: int_x = {int_x}, int_y = {int_y}")
    print("(int_y now points to a new memory location)\n")

pointer_explorer()