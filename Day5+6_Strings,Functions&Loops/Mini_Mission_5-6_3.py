'''
Mini Mission 3: Vowel Counter 🅰️🅾️🔍

🎯 Mission Objective:
Count how many vowels (a, e, i, o, u) are present in a sentence given by the user.

✅ Your Mission Requirements:

Input a sentence from the user.
Convert it to lowercase (so that A and a are treated the same).
Loop through each character.
Use a condition to check if the character is a vowel.
Count how many vowels there are.
Print the total count at the end.
'''
import string
def vowel_counter():
    vowel_count = 0
    sentence = input("Please enter a sentence: ").lower()
    sentence = sentence.strip()
    sentence = sentence.translate(str.maketrans('','', string.punctuation))
    clean_sentence = sentence.replace(" ","")
    for char in clean_sentence:
        if char in "aeiou":
            vowel_count += 1
    return vowel_count

result = vowel_counter()

print(f"Total number of vowels: {result}")