'''
MM2 - Custom Exception Crafter:

👉 Task: 
Build a custom exception class and use it in a small function.
Example idea for you to implement:
Create a class TooSmallError(Exception) with a message.
Write a function that checks if a number is less than 10.
If it is, raise TooSmallError.
Otherwise return the number doubled.
'''
class TooSmallError(Exception):
    "Custom Exception class."
    pass

def num_check(num):
    if num < 10:
        raise TooSmallError("Number is less than 10.")
    else:
        return num * 2

try:
    print(num_check(9))
except TooSmallError as e:
    print(f"Error: {e}")

'''
Advanced version
'''

class TooSmallError(Exception):
    '''Custom Exception for numbers smaller than 10'''
    
    def __init__(self, num, message="Number is less than 10."):
        self.num = num
        self.message = message
        super().__init__(f"{message} Value given: {num}")

def num_check(num):
    if num < 10:
        raise TooSmallError(num)
    return num * 2


try:
    print(num_check(5))
except TooSmallError as e:
    print(f"Caught {e}")
    print(f"Value stored in the exception: {e.num}")