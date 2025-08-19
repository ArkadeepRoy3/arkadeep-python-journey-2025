'''
Write a program that:

Asks the user for a sentence

Prints:

The sentence in uppercase and lowercase
The total number of characters (excluding spaces)
The sentence with the word “Python” replaced with “Java”
The first and last characters of the sentence
'''

sentence = input("Please enter a sentence:")

print("Sentence in Uppercase:", sentence.upper())
print("Sentence in Lowercase:", sentence.lower())
without_white_space = sentence.replace(" ", "")
print("Total number of characters in the sentence excluding white spaces is:", len(without_white_space))
print("The final sentence with the word Python replaced with Java:", sentence.replace("Python", "Java"))
print(f"The first character of the sentence is {sentence[0]} and the last character of the sentence is {sentence[-1]}.")
print("The sentence in reverse order is:", sentence[::-1])