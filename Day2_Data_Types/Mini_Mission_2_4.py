'''
Write a Python program that:

Takes one sentence as input from the user

Then prints:

The first 5 characters
The last 5 characters
The sentence without the first and last character
The sentence reversed
Whether the word "Python" is in the sentence (case-insensitive check)
'''

sentence = input("Enter a sentence:")

print(f"The first 5 characters are : {sentence[0:5]}")
print(f"The last 5 characters are : {sentence[-5:]}")
print(f"Middle section (no first & last char): {sentence[1:-1]}")
print(f"Reversed sentence: {sentence[::-1]}")
if("python" in sentence.lower()):
    print("Contains 'Python'? Yes")
else:
    print("Contains 'Python'? No")