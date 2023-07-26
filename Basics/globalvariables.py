# knowing global and local scope of variable is necessary for a programmer

# global scope of a variable
# -->checkout example below



x = "fantastic"
# the variable above is a globally scoped variable and can be accessed from anywhere...

def myfunction():
    # the variable below is a local scope variable and it can be accessed inside the function only...
    x = "fantasticaaa"  
    print("python is very " + x) 
 

print("python is " + x)
myfunction()


# As you noticed above we used variables of same name but there scope was different and when we accessed x of global scope was different than x of function (local scoped)..


# yet we can also make a local scoped variable a global scoped...
# python help us by provide built in keyword "  global  " see example below

def myfunc():
  global y
  y = "awesome"

myfunc()

print("Python is " + y)
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.
# another word is nonlocal
# that also mean global
