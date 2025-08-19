'''
Ask the user to enter a sentence. Then:

Capitalize the sentence (first letter uppercase, rest lowercase).
Title-case the sentence (first letter of each word uppercase).
Replace all commas , with semicolons ;.
Count how many words are in the sentence.

Bonus 💡: If the sentence ends with a period (.), say "This is a proper sentence."
Otherwise, say "This sentence doesn't end properly."
'''

import string

sentence = input("Enter a sentence:")
clean_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
words = clean_sentence.split()

print(f"Capitalize: {sentence.capitalize()}")
print(f"Title Case: {sentence.title()}")
print(f"Replaced Commas: {sentence.replace(",",";")}")
print(f"Word Count: {len(words)}")

if sentence[-1] == ".":
    print("This is a proper sentence.")
else:
    print("This sentence doesn't end properly.")