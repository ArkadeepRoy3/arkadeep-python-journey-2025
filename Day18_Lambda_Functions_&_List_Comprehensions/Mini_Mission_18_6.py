'''
MM6 - Reverse String List
Task:
Write a program that takes a list of words and uses list comprehension to reverse each word in the list.

Example:

Input: ["python", "rocks", "lambda"]  
Output: ["nohtyp", "skcor", "adbmal"]
'''
word_list = (x.strip() for x in input("Enter words for the list separated by comma: ").strip().split(","))
reverse_word_list = list(map(lambda word: word[::-1], word_list))

print(reverse_word_list)