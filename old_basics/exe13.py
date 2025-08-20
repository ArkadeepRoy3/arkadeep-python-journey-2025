#Given a sequence numbers print the median of the sequence. Note: your solution should work if the sequence is a list or tuple.

numbers = [1,2,3,4,5,6,7,8,9]
median = numbers[len(numbers)//2]
print(median)

numbers = (1,2,3,4,5,6,7,8,9)
median = numbers[len(numbers)//2]
print(median)


numbers = [1,2,3,4,5,6,7,8]
print("Original list is :",numbers)
numbers.sort()
mid = len(numbers)//2
res = (numbers[mid] + numbers[~mid])/2

print("Median of the list is:",res)


numbers = (1,2,3,4,5,6,7,8)
print("Original list is :",numbers)
snum = sorted(numbers)
mid = len(snum)//2
res = (snum[mid] + snum[~mid])/2

print("Median of the list is:",res)
