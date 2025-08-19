'''
Advanced Sentence Play

✅ Tasks:
Take a sentence input from the user

Clean the sentence by removing all punctuation and extra spaces

Convert the sentence to lowercase

Split the sentence into words

Count the number of unique words

Display the total word count and the unique word count

Print each unique word with how many times it appeared
'''
import string

sentence = input("Enter a sentence:")

clean_sentence = sentence.translate(str.maketrans('', '', string.punctuation))

lower_case = clean_sentence.lower()

words = lower_case.split()

#create an empty dictionary 

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else: 
        word_freq[word] = 1


print(f"Total words: {len(words)}")
print(f"Unique word count: {len(word_freq)}")
print("\nWord Frequencies:")
for word, count in word_freq.items():
    print(f"{word} -> {count} times(s)")