'''
MM5 - Partition Play

Task:

Take the string:

text = "Day19-Partition-Play"
Use .partition("-") and print the result.
Use .rpartition("-") and print the result.
Compare the difference in output — notice that .partition() splits at the first occurrence, and .rpartition() splits at the last occurrence.
'''
text = "Day19-Partition-Play"
print(text.partition("-"))
print(text.rpartition("-"))