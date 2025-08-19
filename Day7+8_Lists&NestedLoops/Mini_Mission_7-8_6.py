'''
📈 Mini Mission: List Stats
🎯 Objective:
Given a list of numbers (entered by the user), compute:

✅ Count of numbers
✅ Sum of all numbers
✅ Minimum value
✅ Maximum value
✅ Average

Average

🧪 Your Task:

Write a program that:
Asks the user how many numbers they want to enter.
Takes that many inputs and stores them in a list.
Then, prints all the stats as shown below.
'''
def user_input():
    user_list = []
    input_number = int(input("How many numbers would you like to input?: "))
    for i in range(input_number):
        number = float(input(f"Enter number {i+1}: "))
        user_list.append(number)
    return user_list

def list_stats(list):
    count = len(list)
    total = sum(list)
    min_list = min(list)
    max_list = max(list)
    avg = total/count
    return count, total, min_list, max_list, avg

def print_stats():
    list = user_input()
    count, total, min_val, max_val, avg = list_stats(list)

    print("📊 List Statistics:")
    print(f"- Count: {int(count)}")
    print(f"- Sum: {total:.2f}")
    print(f"- Minimum: {min_val:.2f}")
    print(f"- Maximum: {max_val:.2f}")
    print(f"- Average: {avg:.2f}")

print_stats()