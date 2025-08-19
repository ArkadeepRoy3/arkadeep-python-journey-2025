'''
🧪 Mini Mission 8: Word Collector
🎯 Goal
Write a program that collects words from the user and stores them in a list. After all words are entered, display the full list and show how many words were entered in total.

📘 Pyro's Mission Brief
Use a while loop or for loop to collect words.
Ask the user how many words they want to enter.
Store each word in a list.
After collecting all the words:
Print the full list.
Show the total number of words.
'''
words = []

no_of_words = int(input("Please enter the number of words that you would like to input: "))

for i in range(no_of_words):
    word = input(f"Please enter word {i+1}: ")
    words.append(word)

print(f"You entered {len(words)} words.")
print("📦 Word List: ")
for word in words:
    print("-", word)