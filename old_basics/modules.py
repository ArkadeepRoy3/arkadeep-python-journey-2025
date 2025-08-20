from random import randint
numbers = {1: "one", 2: "two", 3: "three", 4: "four"}
x = randint(1,4)
print(numbers[x])

#If the range of randint is too big, using a dictionary to map numbers to words might not be practical. In that case, you can use a library like num2words which can convert numbers to words.

from random import randint
import num2words

x = randint(1,100)

print(num2words.num2words(x))

#Another important module is the math module.  It provides access to many mathematical functions and constants that you would find on a calculator. Such as math.pi.

import math

print(math.pi)

from math import sqrt

print(sqrt(9))

#The os module provides access to functions that allow you to interact with the operating system, like working with files and directories. Another feature is the ability to read environment variables set by the operating system.

import os
print(os.getenv('PATH'))

import os 
print(os.getenv('HOME'))