#Guess My Type

input_1 = input("Enter an integer value:")
input_2 = input("Enter a float value:")
input_3 = input("Enter a string value:")

input_1 = int(input_1)
input_2 = float(input_2)

print(f"You entered {input_1} which is of type {type(input_1)}")
print(f"You entered {input_2} which is of type {type(input_2)}")
print(f"You entered {input_3} which is of type {type(input_3)}")