def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a/b

if __name__ == "__main__":
    print(f"Test case 2+2: {add(2,2)}")
    print(f"Test case 2-2: {subtract(2,2)}")
    print(f"Test case 2*2: {multiply(2,2)}")
    print(f"Test case 2/2: {divide(2,2)}")