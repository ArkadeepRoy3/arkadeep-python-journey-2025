'''
🔥 Warm-up Recap Problems
1. Lambda + filter/map

👉 Write a function using lambda and filter that returns only even numbers from a given list.

Example:

nums = [1, 2, 3, 4, 5, 6]
# output → [2, 4, 6]
'''

nums = [1, 2, 3, 4, 5, 6]
even_list = filter(lambda x: x % 2 == 0, nums)
print(list(even_list))

'''
2. String Methods

👉 Take this string:

text = "   Hello, Python World!!!   "

Perform these in one script:

Strip spaces.
Replace "World" with "Arka".
Split by comma , and then join with "-".
Expected result: "Hello- Python Arka!!!"
'''
text = "   Hello, Python World!!!   "
new_text = text.strip().replace("World", "Arka").split(",")
clean_text = ("-").join(new_text)
print(clean_text)

'''
3. Context Manager (File Handling refresher)

👉 Using with, write to a file warmup.txt:

Day 18 Warm-up Done!

Then read it back and print the content.
'''

with open("warmup.txt", 'w') as file:
    file.write("Day 18 Warm-up Done!")

with open("warmup.txt", 'r') as file:
    content = file.read()
    print(content)