'''
Mini Mission 5 - Set Analyzer
🎯 Goal: Analyze a dataset using set operations like union, intersection, and difference.

🔧 Mission Brief:
Two groups of students attended two different coding workshops. You're tasked with analyzing their attendance.

workshop_A = {"arka", "ria", "samit", "john", "nina"}
workshop_B = {"ria", "tara", "john", "dev", "meera"}

🛠️ Your Tasks:
Write a program that does the following:

✅ **Print all students who attended at least one workshop.
✅ **Print students who attended both workshops.
✅ **Print students who attended only **Workshop A.
✅ **Print students who attended only **Workshop B.
'''

def analyze_workshops(workshop_A, workshop_B):
    at_least_one = workshop_A ^ workshop_B
    both = workshop_A & workshop_B
    only_A = workshop_A - workshop_B
    only_B = workshop_B - workshop_A

    print("Students who attended at least one workshop: " + ", ".join(item.title() for item in sorted(at_least_one)))
    print(f"Students who attended both workshops: " + ", ".join(item.title() for item in sorted(both)))
    print(f"Students who attended only workshop A: " + ", ".join(item.title() for item in sorted(only_A)))
    print(f"Students who attended only workshop B: " + ", ".join(item.title() for item in sorted(only_B)))

workshop_A = {"arka", "ria", "samit", "john", "nina"}
workshop_B = {"ria", "tara", "john", "dev", "meera"}

analyze_workshops(workshop_A,workshop_B)