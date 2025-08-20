#Python has many built-in functions. These functions are available without importing any modules.

#Numbers

#abs() - returns the absolute value of a number
#round() - rounds a number to a given number of decimals 
#divmod() -  returns both // and % in a singe operation

abs(5)
round(1.234)
divmod(10,3)

#min() - returns the smallest number in the list
#max() - returns the largest number in the list
#sum() - returns the sum of all the numbers in a list

x = [1,2,3,4,5]
min(x)
max(x)
sum(x)

#The ord() and chr() functions allow you to convert a character to and from its Unicode code interger representation.

ord('a')
chr(97)

#Booleans

#Let's break down the behavior of the bool(), any(), and all() functions in Python with the examples given.
#bool() Function
#The bool() function converts a value to a Boolean (True or False) based on its truthiness:

#Zero values (like 0) are considered False.
#Non-zero values (like 1) are considered True.
#Empty objects (like '', [], {}) are considered False.
#Non-empty objects (like 'a', [1], {'key': 'value'}) are considered True.

bool(0)
bool(1)
bool('')
bool('a')

#any() Function
#The any() function returns True if at least one element in the iterable is True. If all elements are False, it returns False.

any([True,False,False])
any([False,False,False])
any(['','',''])
any(['c','b','a'])

#all() Function
#The all() function returns True only if all elements in the iterable are True. If any element is False, it returns False.

all([True,False,False])
all([False,False,False])
all([True,True,True])
all(['','',''])
all(['c','b','a'])

#Sequences

#Several functions can be used to work with sequences. sorted() and reversed() return a new list with changed order. The orginal list is not modified.

x = [2,3,1,4]
sorted_list = list(sorted(x))
print(sorted_list)
reveresed_list = list(reversed(sorted_list))
print(reveresed_list)

#enumerate()
#enumerate function is used to iterate over a sequence when you need both the index and the value.

x = ['a','b','c','c','b','a']
for i, v in enumerate(x):
    print(i,v)
    if i != 0 and v == x[i-1]:
        print("two of the same value in a row")


#