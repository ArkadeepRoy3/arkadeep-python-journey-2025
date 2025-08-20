numbers = (1,1,2,3,4,5,6,7,7,7)
print(numbers)
counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
print(counts)