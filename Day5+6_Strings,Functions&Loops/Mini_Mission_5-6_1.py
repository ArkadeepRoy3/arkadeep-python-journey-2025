'''
🔁 Mission 1: Word Reverser
📝 Task:

Ask the user to input a word.
Reverse the word using string slicing.
Print the reversed word.
Wrap it in a function called reverse_word().
'''

def reverse_word():
    word = input("Please enter the word you want to reverse: ")
    reverse = word[::-1]
    print(f"Reversed word is : {reverse}")
    return reverse

reverse_word()

#Practicing return 

def square(num):
    return num * num

result = square(6)
print(result)

def greet(name):
    return f"Hello, {name}! Welcome aboard."

message = greet("Pyro")
print(message)