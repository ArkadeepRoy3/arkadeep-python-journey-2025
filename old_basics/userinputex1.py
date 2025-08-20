question = input("Would you like a cup of coffee?")
answer = question.strip().lower()
if answer == 'yes':
    print("Excellent!")
elif answer == 'no':
    print("Would you like a cup of tea?")
else:
    print("Would you like anything else?")