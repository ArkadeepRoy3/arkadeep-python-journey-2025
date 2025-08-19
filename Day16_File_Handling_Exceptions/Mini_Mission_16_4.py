'''
🔐 MM4 - Safe Writer
Objective: Practice using try, except, else, and finally while safely writing to a file.

🧩 Specifications:

Prompt the user for a valid .txt filename.
Ask the user to enter a line to write.
Use try/except/else/finally to:
Attempt opening the file in write mode.
Write the input line into the file.
In the else block, print “✅ Write successful!”
In the finally block, print “🧾 Operation complete.”
Handle FileNotFoundError or any IOError gracefully.

Sample:

🔹 Enter the filename: notes.txt  
🖊️ Enter a line to write: Learning never exhausts the mind.

✅ Write successful!  
🧾 Operation complete.

Or, in case of error:

🔹 Enter the filename: readonly:/system.txt  
🖊️ Enter a line to write: This might fail.

❌ Could not write to file.  
🧾 Operation complete.
'''

def safe_writer():
    filename = input("Enter a filename: ").strip()

    if not filename.endswith('.txt'):
        raise ValueError("Only .txt file allowed")
    
    input_line = input("Enter a line to write: ").strip()
    
    try:
        with open(filename, 'w') as file:
            file.write(input_line)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Could not write to file.")
    else:
        print("✅ Write successful!")
    finally:
        print("🧾 Operation complete.")

safe_writer()