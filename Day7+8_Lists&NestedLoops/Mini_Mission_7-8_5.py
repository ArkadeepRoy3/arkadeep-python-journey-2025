'''
🧪 Mini Mission: Palindrome Checker (List Version)
🎯 Objective: Check if a word or sentence is a palindrome using list techniques.

✅ Your Mission
Write a function palindrome_checker() that:

🧾 Input:

Enter a word or sentence: A man, a plan, a canal, Panama

🖨️ Output:

✅ It is a palindrome!
or
❌ Not a palindrome.
'''
import string

def palindrome_checker():
    input_list = []
    sentence = input("Enter a word or sentence: ")
    clean_sentence = sentence.translate(str.maketrans('','', string.punctuation)).lower().strip()
    clean_sentence = clean_sentence.replace(" ","")
    input_list.append(clean_sentence)
    
    if input_list[0] == input_list[0][::-1]:
        print("✅ It is a palindrome!")
    else:
        print("❌ Not a palindrome.")

palindrome_checker()