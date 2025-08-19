'''
MM4 - Word Length Dict → Dict comprehension mapping words to lengths

Goal:

Take a sentence from the user, split it into words, and create a dictionary where:
Keys = the words
Values = the length of each word

Example Input:

Python is powerful

Example Output:

{'Python': 6, 'is': 2, 'powerful': 8}

Bonus Twist:
Ignore punctuation so "Python," still counts as "Python".
'''
import string
sentence = input("Enter a sentence: ").strip()
clean_sentence = sentence.translate(str.maketrans('','',string.punctuation))

sentence_list = clean_sentence.split()

word_dict = {word: len(word) for word in sentence_list}

print(word_dict)