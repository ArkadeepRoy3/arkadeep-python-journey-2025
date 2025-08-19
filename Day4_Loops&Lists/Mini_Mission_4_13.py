'''
✅ First up: Mini Mission 13 – Word Length Counter
Objective:
Take a list of words from the user and print each word along with its length.
'''

word_list = []
length_list = []

number = int(input("Enter the number of words that you want to enter: "))

for i in range(number):
    word = input(f"Enter word number {i+1}: ")
    word_list.append(word)

for i in range(number):
    length = len(word_list[i])
    length_list.append(length)

print("Word                Length")
for i in range(len(length_list)):
    print(f"{word_list[i]:<10} {length_list[i]:>10}")