numbers = [44,65,87,67,23,45,5,6]
print(numbers)
numbers = list(numbers)

n = len(numbers)
if n % 2 == 1:
    median = numbers[n//2]
else:
    median = (numbers[n//2-1] + numbers[n//2])/2

print(f"Median is {median}")