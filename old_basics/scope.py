x = 5
def print_x():
    global x
    x += 1
    print(x)

print_x() # Output: 6
print(x) # Output: 6
