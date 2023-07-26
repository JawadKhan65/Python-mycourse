# as discussed earlier set is unmutable unordered and restrict duplicate members
# to make a set
myset = {"apple", "banana", "mango"}
print(myset)
print(type(myset))
# set can have multiple data types
thisSet = {"apple", 123,123, 3.4, True}
print(thisSet)

# constructor to make a set

sat = set(("dog","meow",123))
print(sat)
# get length of a set
print(len(sat))
# we cannot access set items as we can in list or tuples but looping
# is a way to check
for x in sat:
    print(x)

    # or
    print("meow" in sat)
    # gives a bool value
    # 


# dont think of changing set items as its name is set :)
# we can add more items in set
sat.add("orange")
print(sat)
# for adding a set into other use update()

sat.update(thisSet)
print(sat)

# removing items from set

# remove()
sat.remove("meow")
print(sat)


# discard()
sat.discard("dog")
print(sat)
# pop() pop[ out random item]
x = sat.pop()
print()

# clear()
sat.clear()
print(sat)
# del for deleting
del sat



# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others