from math_utils import add, subtract, multiply, divide

def get_two_numbers():
    try:
        num1 = float(input("Enter 1st number: ").strip())
        num2 = float(input("Enter 2nd number: ").strip())
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    

def safe_math_mod():
    while True:
        print("Menu:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        choice = input("Choose option number: ").strip().replace(".","")
        
        if choice == "1":
            a, b = get_two_numbers()
            result = add(a,b)
            print(f"{a} + {b} = {result}")
        elif choice =="2":
            a, b= get_two_numbers()
            result = subtract(a,b)
            print(f"{a} - {b} = {result}")
        elif choice =="3":
            a, b = get_two_numbers()
            result = multiply(a,b)
            print(f"{a} * {b} = {result}")
        elif choice == "4":
            try:
                a, b = get_two_numbers()
                result = divide(a,b)
                print(f"{a}/{b} = {result}")
            except ZeroDivisionError:
                print("Cannot divide by zero. Try again!")
        elif choice =="5":
            print("Goodbye!")
            return
        else:
            print("Invalid option number. Try again!")
            
if __name__ == "__main__":
    safe_math_mod()