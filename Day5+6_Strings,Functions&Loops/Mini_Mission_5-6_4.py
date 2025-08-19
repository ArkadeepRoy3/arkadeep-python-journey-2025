'''
🧪 Mini Mission 4 — Word Frequency Counter
Goal:
Write a program that takes a sentence and tells you how many times each word appears in it.

🧠 Concepts Involved:

split() to break a sentence into words
dict to store word → frequency
Looping through the list of words
Optional: lower(), punctuation removal, strip() for clean inputs
'''
import string

def word_frequency_counter():
    word_dict = {}
    input_sentence = input("Enter a sentence: ").lower()
    input_sentence = input_sentence.strip()
    input_sentence = input_sentence.translate(str.maketrans('','', string.punctuation))
    input_sentence = input_sentence.split()
    word_list = input_sentence
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    return word_dict

result = word_frequency_counter()
print(result)