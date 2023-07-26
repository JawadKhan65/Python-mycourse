# same as that of string we can access items in list

thislist = ["apple", "banana", "cherry"]
# uncomment or comment it with ctrl + / in vscode and see output
# print(thislist[1])
# print(thislist[1:])
# print(thislist[0:1])
# print(thislist[0:2])
# print(thislist[:3])
# print(thislist[0:])



# as we discussed in previous chapter that
#  list are order changable and allow multiple same items
# tuple are ordered and unchangable and allow multiple items
# where sets are not order not changable and dont allow multiple same items
# dictionary is ordered changable but dont allow multiple items

# here how chage list items
thislist[2] = "donkey"
print(thislist)

# # change in range 
thislist[0:2] = ["cat", "dog"]
print(thislist)
# # here how can we add another item (insert)

thislist.insert(2, "frog")
print(thislist)
