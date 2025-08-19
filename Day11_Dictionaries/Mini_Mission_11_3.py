'''
🧩 Mini Mission 3: Frequency Counter
🎯 Objective:
Create a program that counts how many times each word appears in a sentence input by the user.

✅ Features to Implement:
Input a sentence
Ask the user to enter a sentence (ignore case and strip extra spaces).

Count each word's frequency
Use a dictionary to map:
"word" → number of times it appears

Display the result
Show all words and how many times they appeared.
'''

def freq_counter():
    input_string = input("Enter a sentence: ").lower().strip().split()
    final_dict = {}
    for word in input_string:
        if word in final_dict:
            final_dict[word] += 1
        else:
            final_dict[word] = 1
    print(final_dict)

freq_counter()