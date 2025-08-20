'''x = 21
print("x is", x)
i = 0
for i in range(x):
    if i % 2 != 0:
        continue
    if i <= 20:
        print(i)
    else:
        break'''
# OR 

x = 21
for i in range(x+1):
    if i > 20:
        break
    if i % 2 != 0:
        continue
    print(i)
