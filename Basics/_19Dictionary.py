# dictionary is unordered changable but dont allow duplicate members

# Dictionaries are used to store data values in key:value pairs.

# Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# access by key
print(thisdict["model"])
print(thisdict["brand"])
print(thisdict["year"])

# constructor
mydict = dict(name ="jaw", age = 34, country = "norway")
print(mydict)

# accessing by get keys
x = mydict.keys()
print(x)

# by values
y = mydict.values()
print(y)
# by items
z = mydict.items()
print(z)
# change items
print(mydict)
mydict.update({"age":45})
print(mydict)
# add another item
mydict["color"]='white'
print(mydict)
# removing items
# pop
mydict.pop("age")
print(mydict)

# popitem will delete last inserted item in case is color
mydict.popitem()
print(mydict)
del mydict["name"]
print(mydict)

mydict.clear()
print(mydict)


