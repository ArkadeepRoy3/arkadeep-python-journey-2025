'''
🟨 Mini Mission 1: Tuple Slicer

Task:
Take a tuple of numbers as input and return a new tuple with only the elements from index start to end (both inclusive).

Sample Input:

Original Tuple: (10, 20, 30, 40, 50, 60, 70)

Start Index: 2

End Index: 5

Output:

(30, 40, 50, 60)
'''
numbers = tuple(int(x.strip()) for x in input("Enter a tuple of numbers: ").strip().split(","))
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))

final_tuple = numbers[start_index: end_index+1]
print(final_tuple)