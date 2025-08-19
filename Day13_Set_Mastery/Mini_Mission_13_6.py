'''
🎯 Mini Mission 6: Set Stats Generator
🔹 Objective: Given a set of numbers, display basic statistics like count, min, max, and average.
🔹 Focus: Practice with numeric sets and built-in functions.

✅ Requirements:

Ask the user to input numbers separated by commas (e.g., 5, 12, 8, 20, 12, 8)
Convert them into a set (to automatically remove duplicates)

Show the following stats:

Total unique numbers
Minimum number
Maximum number
Average (rounded to 2 decimal places)

🧪 Example Output:

Enter numbers (comma-separated): 5, 12, 8, 20, 12, 8
🔢 Unique Numbers: {8, 12, 20, 5}
📊 Total Count: 4
📉 Min: 5
📈 Max: 20
📐 Average: 11.25
'''
def set_stat_generator():
    numbers = input("Enter numbers (comma-separated): ").strip().split(",")
    unique_numbers = set()
    for number in numbers:
        unique_numbers.add(int(number))
    print(f"🔢 Unique Numbers: {unique_numbers}")
    
    count = len(unique_numbers)
    print(f"📊 Total Count: {count}")
    print(f"📉 Min: {min(unique_numbers)}")
    print(f"📈 Max: {max(unique_numbers)}")

    average = sum(unique_numbers)/count
    print(f"📐 Average: {average:.2f}")

set_stat_generator()