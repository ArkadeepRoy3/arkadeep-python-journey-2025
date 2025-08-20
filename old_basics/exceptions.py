#An exception is an error that occurs during the execution of a program. When an exception occurs, the program stops and an error message is displayed. For example, if we try to divide a number by zero, we will get a ZeroDivisionError exception.

x = 5/0

#Exception Types
#There are several built in exceptions in python. 

#IndentationError

x = 5
y = 6
  z = 7  # IndentationError: unexpected indent

if x > 5:
print("x is greater than 5")

#ValueError

#A ValueError occurs when a function receives a bad argument. For example, the Int function can convert a string to an integer, but only if the string contains a valid integer.

y = int("24")
x = int("hello") #ValueError.

#TypeError.

#A TypeError occurs when an operation is performed between two incompatible types. It can also occur when calling a function with wrong number of arguments.

x = "hello" + 5
int(1,2,3)

#NameError
#A NameError occures when we use a variable that doesn't exist.

print(b)

#IndexError
#An IndexError occurs when you try to get the index of a sequence that is out of range.

x = [1,2,3]
x[5] #IndexError

#KeyError
#A KeyError occures when you try to get the value of a key that doesn't exist.

x = {1:"a",2:"b",3:"c"}
x[5]

#Exception Handling

try:
    print(b)
except:
    print("b is not defined")

#Is is good practice to specify the type of exception that the expect block will handle. Ex:

try:
    print(m)
except NameError:
    print("m is not defined.")

#the try block functions like if statement in which you can have additional except blocks to handle different types of exception, and an else block if no exception occurs. A finally block always executes when the try block is finished.

try:
    print(z)
    5/0
except NameError:
    print("z is not defined.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except:
    print("Something else went wrong!")
else:
    print("Nothing went wrong!")
finally:
    print("The try-except is finished.")


#Getting the exception
#We can use the as keyword to assign the exception object to a variable. We can then access the exception object's properties and methods, such as its message.

try:
    5/0
except ZeroDivisionError as e:
    print(str(e))








