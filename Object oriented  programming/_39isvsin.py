a = [1, 2, 43]
b = [1, 2, 43]

print(a is b)
print(a == b)


# is operator compares the identity of two objects
# == operator compares the values of objectt
# take a simple analogy if you have a iphone and also someone bought of same models specs
# and colours than is operator will return false == will return true

# is is an identity operator that checks for memory location
# print("cx"*30)

# list1 = ["apple", "banana", "cat", "apricot"]
# list2 = ["roll", "samosa","biryani", "golgappa"]
# for new in list1:
#     for x in list2:
#         print(x,new)
#         # print(new)    
# for x in range(1,11):
#     print(x*2)

# lss = [2, 3, 4 ,5 ,6, 7 ,8 , 9]
# lss2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in lss:
#     for y in lss2:
#         print(x,"X",y, y*x)

# for x in range(1, 21):
#     print(f"4 X {x} = {4*x}")
# range(start, end, step size)

# for x in range(1, 10, 2):
#     print(x)
# z = 2
# r = 3
# while r>z:
#     print("run it ")
#     # z +=1
#     break


def myfunc():
    x =1
    print("O"*20)
    while 10 > x:
        print("X"+" "*18 + "X")
        x+=1
    
    print("O"*20)

for x in range(1, 4):
    print(x,":")
    myfunc()
