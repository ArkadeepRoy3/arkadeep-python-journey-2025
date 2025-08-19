'''
🧪 Mini Mission 6 - Palindrome Checker
🧠 Goal:
Write a function that checks whether a word is a palindrome (reads the same forward and backward).

🛠️ Your Task:

Create a function called is_palindrome()
Take input from user inside the function
Clean the input (convert to lowercase, strip spaces if you want)
Compare the original string with its reversed version
Return an appropriate message
'''
import string

def is_palindrome():
    word = input("Enter a word to check if it's a palindrome or not: ").lower()
    word = word.translate(str.maketrans('','', string.punctuation))
    word = word.strip()
    word = word.replace(" ","")
    reverse = word[::-1]
    if word == reverse:
        return "Yes it is a palindrome!"
    else:
        return "It is not a palindrome!"

result = is_palindrome()
print(result)