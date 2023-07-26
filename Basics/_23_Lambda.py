# a lambda is anonymous function
# a lambda function can take any number arguments,
# but can have only one expression


# syntax lambda arguments : expression
x1 = lambda a : a + 10
print(x1(4,5))

x = lambda a, b : a + 10 + b
print(x(4,5))


# example

def myfunc(n):
    return lambda a: a*n

# lets make it a doubler function

doubler = myfunc(2)
print(doubler(40))

# returns 80