'''
🎯 MM3 Task

Create a class Logger.
In __enter__, print: "Starting block...".
In __exit__, print: "Exiting block...".
Inside the with block, print: "Doing some work".
'''
class Logger:
    def __enter__(self):
        print("Starting block...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"An exception occured: {exc_type.__name__} - {exc_value}")
        print("Exiting block...")
        return True
    
with Logger() as obj:
    print("Doing some work")
    1/0
    print("This will not run")