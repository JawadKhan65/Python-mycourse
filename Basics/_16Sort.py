# sort method as the name show used for sorting items

# in case of string it will sort alphanumerically or in integers numerically

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist1.sort()
print(thislist1)


# copy method to copy a list 
list = thislist1.copy()
print(list)

# we used extend method to add to list we can also use + to add
print("check below")
a = list + thislist
print(a)

list.extend(thislist1)
print(list)

# some more list methods are
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()