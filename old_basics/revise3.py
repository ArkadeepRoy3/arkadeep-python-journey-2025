#positional arguments

def hello(first, last):
    print("Hello", first, last)

hello("arka", "deep")

# Write a function named add that takes two arguments and prints their sum.

def add(x,y):
    sum = x + y
    return sum

result = add(10,20)
print(result)

#keyword argument 

def hello(first, last):
    print("Hello",first, last)

hello(last="deep",first="arka")


def hello(first,last="deep"):
    print("Hello",first,last)

hello("arka")

# / and * are used to specify where the positional and keyword arguemnts start, respectively 

#def test(positional_arg, /,posi_arg_or_keyword_arg, * ,keyword_arg):
    #code block

#The first two arguments are positional arguments and the last two are keyword arguments. The print function can take any number of positional arguments, but there are only a few keyword arguments. Here is what the help function says about the print function.
