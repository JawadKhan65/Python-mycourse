a = "HelloWorld"
# String slicing
print(a[2:])
# in programming index start from 0 and in example it will print from index 2 to forward
# we can convert to uppercase


print(a.upper())
# exacctly the same for lower 
print(a.lower())
# replace method to replace words or charcters
b = "hello" 
print(b.replace("hello","jello"))
# concat strings
print(a + b)
# see output
# and if we want to create a space between it 
print(a + "  " + b)

# find for a word in a string 

string = "hello hey i am robot"
if "hey" in string:
    print("yes it is")

if "honda" not in string: 
    print("no its not")


# note: we cannot add string with a integer directly it will show error
# but format ()method allows you to add

age = 38
txt = "my name is khan, and i am {}"
print(txt.format(age))
# format method take arguments in above case age was argument
# we can add multiple arguments like this
name = "jawad"
club = 333
id = "left322"
txt1 = "my name is {}, and i am {}, my club is {}  and id {}"
print(txt1.format(age, name, id, club))

        #0123456789
block = "blockChain"
        #-10-9-8-7-6-5-4-3-2-1
# [start: stop : skip]
print(block[0:9:2])

#skipping stop limit
print(block[0::2])
print(block[-10]) # b

print(block[::-2])

print(block[-1:-10:-4])

# NOTE: strings are immutable
