'''
Mini Mission 8: Simple Word Analyzer
✅ Objective:
Take a word as input and analyze it by showing:

Total characters
All characters in uppercase
All characters in lowercase
Whether it starts with a vowel or consonant
Reversed word
Whether it is a palindrome (same forwards and backwards)
'''

word = input("Enter a word:")

print(f"Total Characters: {len(word)}")
print(f"Uppercase: {word.upper()}")
print(f"Lowercase: {word.lower()}")


if word[0].lower() in 'aeiou':
    print("Starts with a vowel? Yes")
else:
    print("Starts with a vowel? No")

print(f"Reversed Word: {word[::-1]}")

if word.lower() == word[::-1].lower():
    print("Is it a palindrome? Yes")
else: 
    print("Is it a palindrome? No")