'''
📁 Mini Mission 1: File Line Counter
🔧 Goal:
Write a Python program that reads a text file and counts how many lines it has.

📥 Input: A filename (user provides via input())

📤 Output:

Total lines: X

✅ Example:
Assume sample.txt contains:

Line one.
Line two.
Line three.

Program Output:
Total lines: 3
'''
def file_line_counter():
    filename = input("Enter the filename (use .txt in the end of the filename): ").strip()
    try:
        with open(filename, 'r') as file:
            total_lines = file.readlines()
            print(f"Total lines: {len(total_lines)}")
    except FileNotFoundError:
        print("File does not exist")

file_line_counter()