thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#  also loop through the index number
for i in range(len(thislist)):
  print(thislist[i])

#   using while loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i+1
  
# List comprehension loop

[print(i) for i in thislist]


fruits = ["cat", "bat", "lat"]
next = []
for x in fruits:
  if "c" in x:
    next.append(x)


print(next)
# what above example mean if c is present in the items than
# append those items to next in this case was only cat..

