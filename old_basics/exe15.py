to_remove = [7,2,2]
print(to_remove)
numbers = set()
for num in range(1,11):
    if num not in to_remove:
        numbers.add(num)

print(numbers)