'''
🧩 Mini Mission 2: Word Analyzer
🔍 Focus: Word-level analysis from raw string input
📦 Skills Used: .split(), .lower(), loops, conditionals, string methods

🎯 Your Task:
Write a program that:
Asks the user to enter a sentence.

Then it should output:

✅ Total number of words
✅ Total number of vowels (a, e, i, o, u)
✅ The longest word in the sentence

🖼️ Example

Enter a sentence:  Python is fun and powerful

Word count: 5
Vowel count: 9
Longest word: powerful
'''

def word_analyzer():
    input_sentence = input("Enter a sectence: ").strip().split()
    total_words = len(input_sentence)
    print(f"✅ Total number of words: {total_words}")

    vowel_counter = 0
    vowel_sentence = "".join(input_sentence).lower()
    for letter in vowel_sentence:
        if letter in 'aeiou':
            vowel_counter += 1
    print(f"✅ Total number of vowels (a, e, i, o, u): {vowel_counter}")

    longest_word = input_sentence[0]
    for word in input_sentence:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"✅ Longest word: {longest_word}")

word_analyzer()