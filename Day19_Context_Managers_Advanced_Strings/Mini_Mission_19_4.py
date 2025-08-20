'''
🧩 Mini Mission 4: Context Manager Creator
Goal: Build your own context manager using @contextmanager from contextlib.

Task:

Create a context manager called my_context.
When entering the block, it should print:
"Entering my context..."
When inside, you can run any code (just a simple print for now).
When exiting, it should print:
"Exiting my context...".
'''
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering my context...")
    yield
    print("Exiting my context...")

with my_context():
    print("Inside the block. Doing some work....")