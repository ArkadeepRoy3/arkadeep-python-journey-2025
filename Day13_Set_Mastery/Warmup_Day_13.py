fav_fruits = {"Mango","Kiwi","Lychee","Grapes","Strawberry"}
fruit_set = set()
for fruit in fav_fruits:
    fruit_set.add(fruit)
print(fruit_set)

fruit_set.add("Papaya")
fruit_set.remove("Strawberry")
print(fruit_set)

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date", "fig"}

print("Common:", set1 & set2)
print("Only in set1:", set1 - set2)
print("All combined:", set1 | set2)