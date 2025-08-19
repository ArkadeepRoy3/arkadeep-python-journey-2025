'''
Day 18 - MM2: Even Filter → Filter even numbers using lambda + filter()

Mission Brief:
Write a program that uses a lambda with filter() to extract only even numbers from a given list.

Goal:

Ask the user to enter numbers comma-separated, then filter out the evens using lambda + filter().
Use filter(lambda x: x % 2 == 0, list) to get even numbers.
Convert the result to a list and print both the original and filtered lists.

Example Input:

Enter numbers separated by commas: 4,7,9,12,18,21
Example Output:

Original list: [4, 7, 9, 12, 18, 21]
Even numbers: [4, 12, 18]
Odd numbers: [7, 9, 21]
'''
input_list = list(map(int, input("Enter numbers separated by commas: ").split(",")))
even_list = list(filter(lambda x: x % 2 == 0, input_list))
odd_list = list(filter(lambda x: x % 2 != 0, input_list))
print(f"Orignial List: {input_list}")
print(f"Even List: {even_list}")
print(f"Odd List: {odd_list}")

#

input_list = list(map(int, input("Enter employee IDs: ").split(",")))
ineligible_list = list(filter(lambda x: x % 2 != 0, input_list))
eligible_list = list(filter(lambda x: x % 2 == 0, input_list))
print(f"Eligible IDs (even-ending): {eligible_list}")
print(f"Ineligible IDs (odd-ending): {ineligible_list}")