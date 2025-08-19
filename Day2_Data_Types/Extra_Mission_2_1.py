'''
Palindrome Sentence Checker
🎯 Your Task:
Write a program that takes a full sentence as input and checks whether it's a palindrome.

A palindrome reads the same backward even if we ignore spaces, punctuation, and case.
'''
import string
sentence = input("Enter a sentence:")

clean_sentence = sentence.translate(str.maketrans('', '', string.punctuation))

clean_sentence = clean_sentence.lower()

clean_sentence = clean_sentence.replace(" ","")

if clean_sentence == clean_sentence[::-1]:
    print("Is it a palindrome? Yes")
else: 
    print("Is it a palindrome? No")