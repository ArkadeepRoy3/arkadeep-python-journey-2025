'''
MM3 - Try-Else-Finally
👉 Write a function that:

Tries to divide two numbers.
If division succeeds, the result should be printed inside the else block.
Regardless of success or failure, a message like "Execution finished." should always print from the finally block.
'''
def div_two_num(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print("Division Successful.")
        return result
    finally:
        print("Execution finished.")

print(div_two_num(10,0))

'''
Unit testing
'''
def test_div_two_num():
    result = div_two_num(10, 5)
    assert result == 2, "10 / 5 should return 5."

    result = div_two_num(10,0)
    assert result is None, "Division by zero should return None."

    print("All test passed.")

test_div_two_num()