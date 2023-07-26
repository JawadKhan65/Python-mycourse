# as same as insert append( is another method) but dont take index append at the end


thislist = ["apple", "banana", "cherry"]
thislist.append("dog")
print(thislist)

# as we add something we can similarly add two lists
thislist2 = ["cat", "bat", "rat"]

thislist.extend(thislist2)
print(thislist)


# removal of items

# remove method
thislist2.remove("cat")
print(thislist2)

# pop method

thislist2.pop(0)
print(thislist2)

# now lets check what is left behind in our list
print(thislist2)

# now del keyword which can also delete whole list or also single item
# check output before and after
print(thislist)
print(thislist2)
del thislist2
del thislist[2]
print(thislist)
# print(thislist2) here it will show error because we have deleted list2


# clear keyword which will not dlete but clear a list
print(thislist)
thislist.clear()
print(thislist)
