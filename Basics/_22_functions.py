# function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function.

# A function can return data as a result.
# creating a function
def myfunc():
    print("hello world")
myfunc()

# we can pass arguments 
def func(firstname, lastname):
    print(firstname + " " + lastname)
func("john", "cena")    
   
#    output : john cena
# what is parameter and arguments

# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:8

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments,
#  you have to call the function with 2 arguments, not more, and not less

# this will show error
# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")



# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example
def  tutu(*names):
    print("my name is " + names[0])

tutu("john","mom","sam")

# you can also add arguments with key value syntax

def goga(fname,lname,gender):
    print("first name: " + fname, "last name " + lname, "gender :" + gender)

goga(fname="popa", lname="moga", gender="cartoon")   

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# example

def notorious(**argument):
    print("first name is :" + argument["fname"])
notorious(fname= "jagga", lname = "tagga")


# default parameter mean predefined 

def conutry(country = "Pakistan"):
    print( "this is :" + country)

conutry()
conutry("Sweden")
conutry("germany")
conutry("rome")