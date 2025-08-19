'''
Day 17 MM6 mission brief:

Mission: Safe Import Tester
Goal: Create a script that imports another module only if it exists and handles the error gracefully if it's missing.

Requirements:

Ask the user to enter a module name (e.g., "math", "random", "my_module").
Try importing it using __import__() or importlib.import_module().
If import succeeds, print "Module '<name>' imported successfully!".
If import fails, catch the exception and print "Module '<name>' not found."
Do not crash the program — handle it safely.

Extra Challenge (Optional):

If the import succeeds, try calling a function from it if it's a known built-in module (e.g., math.sqrt(16)).

Example Run:

Enter module name: math
Module 'math' imported successfully!
Square root of 16 is 4.0

Enter module name: notamodule
Module 'notamodule' not found.
'''
def safe_import_tester():
    module_name = input("Enter a module name: ").strip()
    if not module_name:
        print("No module name entered!")
        return
    
    try:
        __import__(module_name)
        print(f"Module '{module_name}' imported successfully!")
    except ModuleNotFoundError:
        print(f"Module '{module_name}' not found.")
    except ImportError as e:
        print(f"Module '{module_name}' could not be imported: {e}")

safe_import_tester()