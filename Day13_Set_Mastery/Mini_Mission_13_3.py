'''
Mini Mission 3 — Common Interests

Skill Focus: Set intersection, input parsing, lowercase normalization

👩‍💻 Scenario:
Two friends are comparing their favorite hobbies. You need to help them find out which hobbies they have in common.

✅ Your Task:
Write a program that:

Asks both friends to enter their hobbies (comma-separated).
Converts both inputs into sets (cleaning up whitespace and casing).
Finds and prints the common hobbies (if any).
Displays a friendly message depending on the result.

🧪 Example:

Enter hobbies of Friend 1: Reading, Music, Coding, Chess
Enter hobbies of Friend 2: Cooking, music, coding, Painting

🎯 Common hobbies: Music, Coding
If no common hobbies:

No common interests found. You both are pretty unique!
'''

def common_interests():
    friend_1 = input("Enter the hobbies of Friend 1: ").lower().strip().split(",")
    friend_2 = input("Enter the hobbies of Friend 2: ").lower().strip().split(",")
    hobbies_set_1 = set()
    hobbies_set_2 = set()
    for hobby1 in friend_1:
        hobbies_set_1.add(hobby1.strip().title())
    for hobby2 in friend_2:
        hobbies_set_2.add(hobby2.strip().title())
    common_hobbies = hobbies_set_1 & hobbies_set_2
    if not common_hobbies:
        print("No common interests found. You both are pretty unique!")
    else:
        print("🎯 Common hobbies:")
        for hobby in sorted(common_hobbies):
            print(hobby)

common_interests()