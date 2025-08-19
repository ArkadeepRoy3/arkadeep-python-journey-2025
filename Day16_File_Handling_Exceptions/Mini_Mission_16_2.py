'''
🧩 Mini Mission 2 - Clean Overwriter
🎯 Objective:
Clean up a .txt file by removing all empty or whitespace-only lines.

✅ Specifications:

Prompt the user for a .txt filename
If the file does not exist, handle it gracefully using try-except

Remove all lines that are:

Completely empty ("")
Only whitespace (e.g., " ", "\t\n")
Overwrite the original file with the cleaned lines
Display how many lines were removed (e.g., 4 lines removed.)

Use:

with for file handling
.strip() to detect empty/whitespace-only lines
try-except for error handling

💡 Hints:

Read all lines using .readlines()
Use a list comprehension to filter out the lines
Use len() to calculate removed lines

🧾 sample.txt (before cleaning):

Hello, this is line one.

This is line three.

     
This is line five.
	
		
▶️ Program Run (Terminal):

Enter the filename: sample.txt
4 lines removed.
File cleaned successfully.

🧾 sample.txt (after cleaning):

Hello, this is line one.
This is line three.
This is line five.
'''
def clean_overwriter():
    filename = input("Enter the filename: ").strip()

    if not filename.endswith('.txt'):
        raise ValueError("Only .txt file allowed.")
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        clean_lines = [line.strip() for line in lines if line.strip()]
        removed_count = len(lines) - len(clean_lines)
        
        with open(filename, 'w') as file:
            for line in clean_lines:
                file.write(line + '\n')
        
        print(f"\nFile cleaned. {removed_count} empty/whitespace lines removed.")
        print(f"\n--- Cleaned Content ---")
        with open(filename, 'r') as file:
            print(file.read())

    except FileNotFoundError:
        print("File not found.")

clean_overwriter()