'''
🧪 Mini Mission 2: Duplicate Finder

Concepts: Using sets to detect duplicates in a list

🔧 Challenge Prompt (Mini Mission 2)

Write a program that:

Takes a list of user-entered names (in one input, comma-separated)
Prints all duplicates only once (case-insensitive)

Example:

Input: Arka, Samit, Ria, arka, RIA, Tara, tara
Output: Duplicates found: arka, ria, tara
'''
def dup_finder():
    user_names = list(input("Enter names: ").lower().strip().split(","))

    seen = set()
    duplicate = set()

    for name in user_names:
        cleaned_name = name.strip()
        if cleaned_name in seen:
            duplicate.add(cleaned_name)
        else:
            seen.add(cleaned_name)
    
    if duplicate:
        print("🔁 Duplicates found:",", ".join(duplicate))
    else:
        print("✅ No duplicates found!")
    
dup_finder()