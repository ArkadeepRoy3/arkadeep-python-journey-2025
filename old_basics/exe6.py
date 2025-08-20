#Given a number x, use continue to print out even numbers from 0 to x. Use break Stop if you reach a number greater than 20.
x = 4
print('x is', x)

for i in range(0,x):
    if i > 20:
        break
    if i % 2 != 0:
        continue
    print(i)