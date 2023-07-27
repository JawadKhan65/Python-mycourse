print("Decorators")
#  decorator is very power full 

# tool used for modifying a function without changing its source code

#  a decorator function takes a function as an argument and return a

# new function that modify orignal function. the new function is refered

# as decorated function
# closure function
def decorator(argu_func):
    def newfunc():
        print("GOOd HOW are YOu")
        argu_func()  
        print("Thanks for using this function")
    return newfunc  # return a new function



# def nobfun(argfun):  # example 2
#     def nefun():
#         print("decorator")
#         argfun()
#         print("thanks for using")
#     return nefun

# @decorator  # least preferd


def hello():
    print(f"hey hello Mr ")


# hello()   #using decorator as @decorator is not a good practice but it is easy 
# using it like this would be good

decorator(hello)()  # highly prefered

# nobfun(hello)()   #example 2


