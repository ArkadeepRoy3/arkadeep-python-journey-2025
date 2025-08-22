'''
⚡ MM1: Raise It Up

Write a function that takes a number.
If the number is negative → raise ValueError("Negative not allowed").
If the number is not an integer → raise TypeError("Only integers allowed").
Otherwise → return the number doubled.
'''
def raise_it_up(num):
    if isinstance(num, int):
        if num >= 0:
            return num * 2
        else:
            raise ValueError("Negative not allowed.")
    else:
        raise TypeError("Only integers allowed.")

print(raise_it_up(2))