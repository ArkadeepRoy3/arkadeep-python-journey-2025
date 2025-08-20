#Data structures is a way to store data. Different data structures are used for different tasks.

#List
#A list is a data structure that stores ordered data. It also allows us to add and remove data, as well as sort the data.

numbers = [4,2,3,1]

numbers.append(5)
numbers.append(6)
numbers.remove(6)
numbers.sort()
print(numbers)

#Tuple
#A tuple is a data structure that stores ordered data. It is immutable, meaning that once created, it cannot be changed.

numbers = (1,2,3)
print(numbers)

#This may look familiar to you because function arguments are passed as tuples.
#Also, if you return multiple values from a function, they are returned as a tuple.

def add_and_subtract(a,b):
    return a + b, a - b

result = add_and_subtract(10,5)
print(result) #the result is printed as tuple.

#To modify a tuple, you need to convert it to a list and then modify the list.

numbers = (1,2,3)
numbers = list(numbers)
numbers.append(4)
print(numbers)

#Sequence
#A sequence is a data structure that stores ordered data. List and tuple are sequences. String is also a sequence. A sequence is an ordered collection of items that can be accessed by index. There are several operations you can do with a sequence.

#Indexing
#A data element in a sequence can be accessed by its index. The first element in a sequence has an index of 0.

letters = "abcdef"
numbers = [1,2,3,4,5]
other_numbers = (6,7,8,9)

print(letters[0])
print(numbers[0])
print(other_numbers[0])

#Python also has support for negative indexing, which allow you to access elements from the end of the sequence.

print(letters[-1])
print(numbers[-1])
print(other_numbers[-1])

#Slicing
#You can also use indexing to create a new sequence from a subset of the original sequence. This is called slicing.

letters = "abcdef"
numbers = [1,2,3,4,5]
other_numbers = (6,7,8,9)

print(letters[1:3])
print(numbers[1:3])
print(other_numbers[1:3])

numbers = [1,2,3]
print(numbers[:2])
print(numbers[1:])

#Iterating
#Iterating is the process of going through each element in a sequence. You can do this with a for in loop.

letters = "hello"
for letter in letters:
  if letter == "l":
    print("found l")

numbers = [1,2,3,4,2,3,2,2]
count = 0
for number in numbers:
   if number == 2:
      print("found 2")
      count += 1
print("Total number of 2's are:",count)

#OR

numbers = [1,2,3,4,2,3,2,2]
count = numbers.count(2)
print("Total number of 2's are:",count)

#Concatenation
#You can also combine two sequences using the + operator. We can see this with strings already, but it also works with lists and tuples.

letters = "hello"
numbers = [1,2,3,4]
other_numbers = (6,7,8,9)

print(letters + "there")
print(numbers + [5,6,7])
print(other_numbers + (10,11,12))

#Concatenation only works with sequences of the same type. You cannot combine a list and a tuple.

#in operator

numbers = [1,2,3,4]
print(1 in numbers)
print(5 in numbers)

#len function
#We can get the length of a sequence using the len function.

numbers = [1,2,3,4]
print(len(numbers))

#Sequence Unpacking and Assignment

numbers = [1,2,3,4]
a,b,c,d = numbers
print(a)
print(b)
print(c)
print(d)

#You don't have to assign all the values in the sequence. You can use the _ character to ignore values and the * character to capture the rest of the values.

numbers = [1, 2, 3, 4, 5]
a, _, b, _, c, *d = numbers
print(a)
print(b)
print(c)
print(d)

#Set
#A set is a data structure that stores unordered data. It allows us to add or remove data as well as check if the data is present in the set.We can create a set using the set function or by using curly braces. If we want to create an empty set, we will need to use the set function.

numbers = set([1,2,3,4])
print(numbers)

letters = {"a","b","c","d"}
print(letters)

#A set can only have unique values. If we try to add a value that is already present in the set, the value will be ignored.

numbers = set([1,2,3,4])
numbers.add(1)
print(numbers)

#Basic operations to do with a set
numbers = {1,2,3}
numbers.add(4)
print(numbers)
numbers.remove(4) #error if 4 is not in the set but since it was previously added, it will be fine.
print(numbers)
numbers.discard(4) #does not error if 4 is not in the set
print(numbers)
numbers.clear()
print(numbers)

#Sets are unordered, so you cannot access a specific value in a set. However, several of the same operations that work for sequences also work for sets.

numbers = {1,2,3}
print(len(numbers))
print(1 in numbers)
for number in numbers:
   print(number)

#Sets also have some useful operations that can be used on multiple sets.

numbers = {1,2,3}
other_numbers = {4,5,6,7}

print(numbers | other_numbers) #union
print(numbers & other_numbers) #intersection
print(numbers - other_numbers) #difference
print(numbers ^ other_numbers) #symmectric difference

#Dictionary
#A dictionary is a data structure that stores data in key-value pairs. You can create a dictionary using the dict function or by using curly braces.

letters = {1:"a",2:"b",3:"c"}
print(letters)

numbers = dict([(1,"one"),(2,"two"),(3,"three")])
print(numbers)

empty = {}

#A dictionary can only contain unique keys, this is similar to a set. However, the values in a dictionary can be repeated.

numbers = {1:"a",2:"b",3:"c",4:"a"}
print(numbers)

#Add or change values to a dictionary by key

numbers = {1:"a",2:"b",3:"c"}
numbers[1] = "One"
numbers[2] = "Two"
print(numbers)

#Using in operator we can check if a key is present in the dictionary

numbers = {1:"a",2:"b",3:"c"}
print(1 in numbers)
print(2 in numbers)
print(4 in numbers)

#Using values operator we can check if a value is present 

numbers = {1:"a",2:"b",3:"c"}
print("one" in numbers.values())
print("a" in numbers.values())

numbers = {1:"a",2:"b",3:"c"}
print(len(numbers))

#You can use the keys method to iterate over the keys in a dictionary or the values method to iterate over the values.

numbers = {1:"a",2:"b",3:"c"}
for keys in numbers.keys():
   print(keys)

numbers = {1:"a",2:"b",3:"c"}
for value in numbers.values():
   print(value)

#However, the items method will give you both the key and value.

numbers = {1: "one", 2: "two", 3: "three"}
for keys, values in numbers.items():
   print(keys,values)




