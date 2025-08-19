import logger_utils as lu
import safe_math_mod as sm

def main():
    print("=== Logging Calculator (MM3) ===")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = sm.add(num1,num2)
        elif operator == "-":
            result = sm.subtract(num1,num2)
        elif operator == "*":
            result = sm.multiply(num1, num2)
        elif operator == "/":
            result = sm.divide(num1,num2)
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")
        lu.log_calculation(num1, operator, num2, result)
        print("Calculation logged successfully.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()