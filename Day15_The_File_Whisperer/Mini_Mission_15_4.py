'''
🛠️ Mini Mission 4: Sanitize File Contents
🔧 Task:
You need to:

Open a .txt file.
Strip leading and trailing spaces from each line.
Replace all occurrences of "Python" with "PyWorld" (case-sensitive).
Save the cleaned version into a new file (ask user for output filename).

📝 Sample Input File:

   Python is fun.    
I love learning Python!    
  Let's master Python together.

✅ Output File Content:

PyWorld is fun.
I love learning PyWorld!
Let's master PyWorld together.
'''
import string

def sanitize_file():
    filename = input("Enter the filename (use .txt at the end of the filename): ").strip()
    output_file = "cleaned_" + filename

    try:
        with open(filename, 'r') as file, open(output_file, 'w') as new_file:
            for line in file:
                cleaned = line.strip().replace("Python", "PyWorld")
                new_file.write(cleaned + '\n')
        print(f"Sanitized content saved to {output_file}")
        print(f"\n--- Cleaned File Contents ---")
        with open(output_file, 'r') as file:
            print(file.read())

    except FileNotFoundError:
        print("File not found.")

sanitize_file()