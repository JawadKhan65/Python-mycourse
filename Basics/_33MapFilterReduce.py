# x = lambda a: a*a*a

# print(x(3))

l = [1, 2, 3, 4, 5, 6]
# # map function takes two arguments one is function and other is on which function is to be applied
# when we call some thing to map it according to that one we are
# saying to relate and colab them just in that same way it works

# newl = map(x, l)

# print(list(newl))

# filter
# just like any filter which filter according to its own function this filter works the same

# def filter_function(a):
#     return a>4
# newnewl = filter(filter_function, l)
# print(list(newnewl))

# reduce its also a higher order but need to be imported
from functools import reduce

sum = reduce(lambda x, y: x + y, l)
print(sum)
# output:21
# how it works have a look
# we have number 
# 1 2 3 4 5 6
# it wil take x,y and give x+y
# first 1 = x, 2 = y --> 1+2 = 3- so reduce it to 3
# now list is as 3 3 4 5 6 ok than furthur take 
# 3 as x 3 as y --> 6 reduced to 6| now list become 6 4 5 6
# again 6 as x ,4 as y . 6+4-->10 | reduced to 10 5 6
# now 10 as x, 5 as y | 10 + 5-->15 | list now  reduced to 15 6  
# 15 is x and 6 is y reduced to 21 
# So i hope its clear how reduce works



