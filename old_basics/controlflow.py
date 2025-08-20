#Boolean and comparison

is_true = True
is_false = False

#if statement

if True:
    print("It is true")


if True: 
    print("This will print")
    print("This will also print")

if False:
    print("This will not be executed")

if x == 10:
    print("This might be printed") #this will be executed only if x equal to 10


#nested if

if True:
    print("This will print")
    if False:
        print("this will not print")
    print("This will also print")

#else and else-if

x = 6
if x > 7:
    print(f"{x} is greater than 7")
else:
    print(f"{x} is less than 7")

#elif

x = 6
if x > 7:
    print("x is greater than 7")
elif x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

#while loop

while True:
    print("This will print over and over again")

times = 3
while times > 0:
    print("This will print 3 times")
    times -= 1

#for loop

for i in range(3):
    print("this will print 3 times")


#break and continue

while True:
    print("This will only print once")
    break

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  #this basically prints all the odd numbers from 0 9 which are 1 3 5 7 9

