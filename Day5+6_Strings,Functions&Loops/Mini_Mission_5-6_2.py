'''
🧪 Mini Mission 2: Clean Sentence
🎯 Goal:
Take a messy sentence from the user and clean it by:

Converting to lowercase
Removing punctuation (e.g., ., !, ,)
Replacing multiple spaces with a single space
Returning the cleaned sentence
'''
import string

def clean_sentence():
    sentence_input = input("Please enter the sentence that you want to clean: ").lower()
    clean_sen = sentence_input.translate(str.maketrans('','', string.punctuation))
    clean_sen = clean_sen.strip()
    clean_sen = clean_sen.split()
    clean_sen = ' '.join(clean_sen)
    return clean_sen

final_sentence = clean_sentence()
print(final_sentence)