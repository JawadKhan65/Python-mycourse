# Classes are the blueprint or templates for creating objects in Python. 
# They define the structure and behavior of objects. A class encapsulates
#  data (attributes) and functions (methods) that operate on 
# that data. It provides a way 
# to organize and structure code in a more modular and reusable manner.


# Constructors and Destructors:
# Constructors and destructors are special methods in a class that allow you to initialize and 
# clean up resources when objects are created and destroyed.
# Constructor: In Python, the constructor is defined as the __init__() method.
#  It is automatically called when an object is created from the class.
#  It is used to set up initial attributes and perform any necessary setup.

# Destructor: The destructor is defined as the __del__() method. It is called when an object is about to be destroyed or deallocated. 
# The primary purpose of the destructor is to release resources or perform cleanup tasks before the object is removed from memory.

# constructor in python

# constructor is the special method in oops

# it  is used to intialize objects properties

# and executed automatically when an object is called

# for writing constructor we use special method called dundar method

# __init__(self)



class Person:
    
    # constructor
    def __init__(self, n, o):
        print("i told you when we call an object mean create an object it constructor is automatically called")
        self.name = n #these are the attributes of class
        self.occ = o
    
    # this is a class method
    def info(self): 
        print(f"{self.name} is a {self.occ}")

# creating object to acess class
a = Person("jack", 'Developer')


a.info()

b = Person("saad", 'PM')
b.info()


# In object-oriented programming (OOP) in Python, 
# "self" refers to the instance of a class.
#  When you create an object from a class in Python, 
# that object is an instance of the class.
#  The "self" parameter is used to refer to that
#  instance within the class definition
# , allowing you to access the instance's attributes and methods.
# here its clear about self but as we remind that in functions
# we studied that if arguments are given to function
# so when we call function we must have to give parameters unless it will
# show error
# line 24 line 27 we gave 2 arguments to function but it was 
# taking three self n o but self is given automatically to object so it takes
# two parameters
# if you give three parameter it will show you errors
# c = Person(1, 2, 3) # #uncomment and run it
