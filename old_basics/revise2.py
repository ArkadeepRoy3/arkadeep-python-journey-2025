#PEMAA
#Parentheses
#Exponent
#Multi and Div
#Add and sub
#Assignment

x = 2
x += 3
print(x)

#if statement executes a block of code only when the boolean expression evaluates to true

if True:
    print("This is true")


if False:
    print("this will not print")
    print("this will also not print")

#nested if 

if True:
    print("this will print")
    if False:
        print("this will not print")
    print("this will also print")

#else and elif

x = 8
if x > 7:
    print("x is greater than 7")
else:
    print("x is less than 7")


x = 5

if x > 7:
    print("x is greater than 7")
elif x == 7:
    print("x is equal to 7")
elif x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

x = 2

if x > 5:
    print("x is greater than 5")
elif x > 7:
    print("x is greater than 7") #this code will never be executed because of the position of the elif statement 
else:
    print("x is less than 5")


#while loop

times = 4
x = 0
while x  < times:
    print("this will print 4 times")
    x += 1

times = 4
while times > 0:
    print("this will print 4 times")
    times -= 1

x = 0
while x < 10:
    print(x)
    x += 1

#for loop using range function

for i in range(3):
    print("this will print 3 times")

#break and continue 

#used in while and for loops to alter their behaviour

while True:
    print("this will only print once")
    break

while True:
    print("this will keep on printing")
    continue
    print("this will never be printed")

#break and continue are often used in conjection with if statements

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


x = 18
for i in range(x):
    if i > 20:
        break
    if i % 2 != 0:
        continue
    print(i)

        
#None value

x = None
if x == None:
    x = "default value"


x = None
y = None
z = 20 
sum = 0
if x != None:
    sum += x
if y != None:
    sum += y
if z != None:
    sum += z
print(sum)


#boolean operations

x = 11 
y = 3
z = 3

if x > 10 and y > 10:
    print("step 1 is", True)
if z > x or y > x:
    print("step 2 is", True)
else:
    print("step 2 is", False)


    