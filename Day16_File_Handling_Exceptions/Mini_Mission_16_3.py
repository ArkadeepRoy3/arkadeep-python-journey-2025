'''
🧩 Mini Mission 3 - File Cloner
🆔 ID: MM3
🎯 Name: File Cloner
📂 Description:
Create a utility that takes a source and destination filename from the user, and copies the content from source to destination.

✅ Specifications:
Prompt for:

Source filename (must be .txt)
Destination filename (must also be .txt)
Use a with block to safely open both files.
If source file doesn't exist, show an error.
If destination already exists, warn the user and ask if they want to overwrite (y/n)
If user says no, cancel the operation.
If yes, write source contents into destination file.
After writing, show a success message with how many lines were copied.
Use structured try/except/else/finally

💡 Tips:

Use .readlines() or loop through line-by-line.
Use os.path.exists() to check if the destination file already exists.
You can count lines using len(lines) or a counter.

🧪 Sample Run:

Enter source filename: notes.txt  
Enter destination filename: backup_notes.txt  

📂 Destination file already exists. Overwrite? (y/n): n  
❌ Operation cancelled.
✅ Another Run:

Enter source filename: notes.txt  
Enter destination filename: backup_notes.txt  

📂 Destination file already exists. Overwrite? (y/n): y  
✅ 8 lines copied from notes.txt to backup_notes.txt  

⚠️ Error Case:

Enter source filename: missing.txt  
Enter destination filename: copied.txt  

❌ Source file not found. Cannot proceed.
'''
import os

def file_cloner():
    source_filename = input("Enter source filename: ").strip()
    destination_filename = input("Enter destination filename: ").strip()

    if not source_filename.endswith('.txt'):
        raise ValueError("Only .txt file allowed.")
    if not destination_filename.endswith('.txt'):
        raise ValueError("Only .txt file allowed.")
    
    try:
        with open(source_filename, 'r') as src_file:
            lines = src_file.readlines()
        if os.path.exists(destination_filename):
            choice = input("📂 Destination file already exists. Overwrite? (y/n): ").lower().strip()
            if choice == "y":
                with open(destination_filename, 'w') as dst_file:
                    for line in lines:
                        dst_file.write(line)
                    copied_lines = len(lines)
                    print("✅ Backup Successful.")
                    print(f"✅ {copied_lines} lines copied from {source_filename} to {destination_filename}")
            elif choice == "n":
                print("❌ Operation cancelled.")
            else:
                print("Please choose either 'y' or 'n'.")
        else:
            with open(destination_filename, 'w') as dst_file:
                for line in lines:
                    dst_file.write(line)
                print("✅ Backup Successful.")
    except FileNotFoundError:
        print("❌ Source file not found. Cannot proceed.")
    finally:
        print("End of operation.")
    

file_cloner()