'''
📄 Mini Mission 3: Keyword Finder
🎯 Goal:
Ask the user for a keyword and a filename.
Then, read the file line-by-line and print only those lines that contain the keyword (case-insensitive).

🧪 Sample Flow:

Enter filename: diary.txt  
Enter keyword to search: dream

Matching lines:
Today I had a strange dream.
My dreams often feel real.
✅ Requirements:

Case-insensitive search
Ignore leading/trailing whitespace
Only print lines where the keyword exists
'''
import string

def keyword_finder():
    filename = input("Enter the filename (use .txt at the end of the filename): ").strip()
    keyword = input("Enter a keyword to search: ").lower().strip()
    translator = str.maketrans('','', string.punctuation)

    try:
        print("Matching lines: ")
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.translate(translator).lower()
                if keyword in clean_line.split():
                    print(line, end="")
    except FileNotFoundError:
        print("File was not found.")

keyword_finder()