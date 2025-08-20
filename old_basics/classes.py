#A class is a data structure that contains attributes and methods. Ex: int and list are classes.

print(int) # <class 'int'>
print(list) # <class 'list'>

#In the list class the attributes are the data that is stored in the list and the methods are the functions that can be called on the list, for example append and sort.

#A class instance is an object created from a class.
#Ex: 1 and 5 would be the instances of int class.

#We can use the built-in function isinstance to check if an object is an instance of a class.
#We can use the type function to get the class of the object.

isinstance(1,int)
isinstance(5,list)

print(type(5))

#Creating a class
#class keyword is used to create a class.

class ClassDef:
    attribute = 10
    def method():
        return 20

print(ClassDef.attribute)
print(ClassDef.method())

#Creating an instance

class ClassDef:
    attribute = 10
    def method(self):
        return self.attribute * 2

class_instance = ClassDef() #use the class to create an object.
print(class_instance.attribute)
print(class_instance.method())

#The __init__ method.
#Dunder methods are special methods that are used to define the behaviour of a class. 
#The __init__ dunder method is one of those special methods.
#It is called when an object is created from a class to initialize the object with any attributes that is required.

class ClassDef:
    def __init__(self,attribute):
        self.attribute = attribute
    def method(self):
        return self.attribute * 2

class_instance = ClassDef(20)
print(class_instance.attribute)
print(class_instance.method())