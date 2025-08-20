#Create a class called Person
#Add two attributes: name and age that can be set when the object is created.
#Create a method called introduce that prints a string in the format:
#Hi, My name is Joe and I am 12 years old.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} and my age is {self.age}")

class_instance = Person("Joe",10)
class_instance.introduce()