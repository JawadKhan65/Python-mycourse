# there are two loops in python 
# 1. While loop
# 2. For loop

# While loop
# With the while loop we can execute a set of statements as long as a condition is true

i = 1 #first give a  initial number

while i < 6:
  print(i)
  i += 1



#   if else statement in loop
# we can use break function to stop loop on a condition



while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# similiarly a continue keyword to continue upon a condition check
# it will step over the cndition in below step 3

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


i=0
while i < 8:
  print(i)
  i += 1
else:
  print("i is no longer less than 8")  


# For Loop in python
# loop through array
fruits = ["apple", "banana", "cat"]
for x in fruits:
  print(x)

# loop through string
a = "bannnanana"
for x in a :
  print(x)


# we can use break and continue here also

for x in fruits:
  print(x)
  if x == "banana":
    break
  
#   continue
for x in fruits:
  
  if x == "banana":
    continue
  print(x)

# for loop with range
for i in range(0, 10):
  print(i)

#   it takes three arguments (0, 10, this will intcrement it with value)
for i in range(0, 10, 2):
  print(i)

# nested loop
fruits2 = ["ball", "myballs", "bobals"]
for i in fruits:
  for x in fruits2:
    print(x, i)