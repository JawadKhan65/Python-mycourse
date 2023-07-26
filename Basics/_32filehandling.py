# opening a file there is keyword open..
#  it take two arguments first name second what you want to do .
# r = read
# if i want to read a binary file i will use rb so you ca also use for example like image pdf etc
# w to write into file if file doesnt exist it wil create new file 
# a for append if file doesnt exist it wil create new file 
# x to create a file if already exist gives a error
# we have to assign a mode of file to read t defines text mode no difference b/w 
# rt , wt


# Reading a file

# f = open("myfile.txt", 'r')
# text = f.read()
# print(text)
# f.close() #it is must to close file after opening

# Writing a file
# f = open('myfile.txt', 'w')
# f.write('hello danger pa g')
# f.close()


# appending a file
# f = open('myfile.txt', 'a')
# f.write('hello danger pa g')
# f.close()
# this will append everytime you run


# Note as i said we must have to close file after opening but there is 
# alot pain in it but there is a keyword with to sort out that
 

# with open("myfile.txt", 'r') as fa:
#     reading = fa.read()
#     print(reading)

# we can also read lines
f = open('myfile.txt', 'r')
# lines = f.readline()
# print(lines)

# i=0
# while True:
#     i+=1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student {i} in math is: {m1}")
#     print(f"Marks of student {i} in english is: {m2}")
#     print(f"Marks of student {i} in science is: {m3}")

