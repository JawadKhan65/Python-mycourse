# tuple as discussed ordered unchangeable

# allow duplicate items
# tuple is also a data type use to store multiple items of any data type
# to make a tuple

tupple = ("apple", "banana", "cherry")
print(tupple)
print(type(tupple))

# tuple item can be of multiple data types

tap = ("apple", "cat","cat", "banana",12, 12.3)
print(tap)

# we can alsp use a tuple constructor to make a tuple

tp = tuple(("cat", "dog", "umberella"))
print(tp)
# find length of a tuple

print(len(tupple))

# like list we can access tuple
print(tupple[0])
print(tupple[0:])
print(tupple[:2])

# we discussed that a tuple is unchangable but list is . so to change a tuple 
# we have to convert it imto a list

# tap is already created tuple
# tap = ("apple", "cat","cat", "banana",12, 12.3)
y = list(tap)
y[1] =  "dog" #changing
# the magic is here that we have changed it into a list then changed it into a tuple

tap = tuple(y)

print(tap)
# if we want to append we will do the same convert to list and again  to tuple
# for removing same...
# adding tuple to tuple

x = tap + tupple
print(x)

# deleting a tuple
del tap
# now print(tap)will show error

# unpack a tuple
fruits = ("apple", "banana", "cherry")

(a, b, c) = fruits

print(a)
print(b)
print(c)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) #red contains all other than apple banana
print("printing")
tupple1 = ("apple", "banana", "cherry")
tupple2 = ("apple", "banana", "cherry")
print(tupple1+tupple2)

