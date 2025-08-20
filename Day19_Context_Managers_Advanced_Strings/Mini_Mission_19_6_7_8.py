'''
String Surgeon (Day 19 Final MM)

Take the messy string:

text = "   data_report.txt\tPython\tRocks-Day19.csv   "

Perform these operations step by step:

Strip it → Use .strip() to remove extra spaces.
Expand tabs → Use .expandtabs(12) to align the tab-separated parts.
Check prefix/suffix →
Does it start with "data"?
Does it end with ".csv"?
Partition magic → Use .partition("-") and .rpartition("-") to split around the dash.
Rebuild → Use " ".join(...) to stitch cleaned parts into a neat sentence.
🎯 Goal: Practice all advanced string methods from today in one challenge.
'''
text = "   data_report.txt\tPython\tRocks-Day19.csv   ".strip().expandtabs(12)

if text.startswith("data"):
    print("Yes! It starts with 'data'")
else:
    print("No! It doesn't start with 'data'")

if text.endswith(".csv"):
    print("Yes! It ends with '.csv'")
else:
    print("No! It doesn't end with '.csv'")

beforeL, spearatorL, afterL = text.partition("-")
beforeR, spearatorR, afterR = text.rpartition("-")
print(f"Before: {beforeL}, Separator: {spearatorL}, After: {afterL}")
print(f"Before: {beforeR}, Separator: {spearatorR}, After: {afterR}")

clean_text = " ".join(text.split())
print(clean_text)