'''
🧠 Day 9 Warm-up: Quickfire Logic & Lists
📌 Task:
Write a function that:

Takes a list of integers from the user
Returns a new list containing only the square of even numbers

🧾 Example Input:

Enter numbers (comma-separated): 1, 4, 6, 7, 9, 10
✅ Output:

[16, 36, 100]
'''
def sq_even():
    number_list = []
    result_list = []
    integer_list = list((input("Enter numbers (comma-separated): ").split(",")))
    for item in integer_list:
        num = int(item.strip())
        number_list.append(num)
    for item in number_list:
        if item % 2 == 0:
            result_list.append(item**2)
    return result_list

result = sq_even()
print(result)