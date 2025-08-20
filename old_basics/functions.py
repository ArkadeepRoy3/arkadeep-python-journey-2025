#Functions
#We use functions to call a block of code from other parts in a program. We can use functions to break down large code into smaller parts.

print("Hello")  #print is a built-in function

#def is the keyword that is used to define a function. Any arguments that the function takes can be defined inside parentheses.

def hello():
    print("Hello World")

hello()

#Arguments can be passed into a function by defining them inside the parentheses

def hello(first, last):
    print("Hello",first, last)

hello("arka", "deep")

#keyword arguments

def hello(first, last="deep"):
    print("Hello",first, last)

hello("Arka")
hello(first="John")
hello("Jz",last="X")

def hello(first="AB",last="BC"):
    print("Hi", first, last)

hello("BC","AB")


def test(position_only, /, postion_or_keyword, *, keyword_only):
    #code block

# / for positional argument and * for keyword argument

print("Hello", "World", sep="-", end="!\n")

# Here 'sep' and 'end' are some of the keyword arguments that can be initialized with print function 

for i in range(10):
    print(i, end=" ")
print()

#Return values

def add(x,y):
    sum = x+y
    return sum
add(10, 20)

#Scope of a variable



x = 10
def add_one():
    global x
    x += 1
    return x

def add_two(x):
    x += 2
    return x

print(add_one())
print(add_two(10))


x = 5
def print_x():
    global x
    x += 1
    print(x)

print_x()


