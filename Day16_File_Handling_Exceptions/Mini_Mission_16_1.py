'''
🧩 Mini Mission 1 - Safe Logger
Objective: Create a robust file backup tool that reads a file, creates a backup, and logs success or failure — using advanced file handling and exception structure.

✅ Mission Requirements

Build a function backup_file() that:
Asks the user for a filename (must end with .txt)
Checks if the file exists
If not, prints: ❌ File not found. Backup failed.

If the file exists:

Creates a backup file named: backup_<original>.txt
Copies all content from the original into the backup
Logs the operation outcome using:
try...except...else...finally

💡 Hints

Use 'r' mode to read original
Use 'w' mode to write to backup

Backup filename can be built like:

backup_name = "backup_" + filename

🧠 Skill Focus

File I/O confidence
Backup logic
Realistic exception control
'''
def backup_file():
    filename = input("Enter a filename: ").strip()
    backup_name = "backup_" + filename

    if not filename.lower().endswith('.txt'):
        raise ValueError("Only .txt file allowed.")
    try:
        with open(filename, 'r') as file, open(backup_name, 'w') as backup:
            for line in file:
                backup.write(line)
    except FileNotFoundError:
        print("❌ File not found. Backup failed.")
    else:
        print("Backup Successful.")
    finally:
        print("End of backup operation.")
    
backup_file()