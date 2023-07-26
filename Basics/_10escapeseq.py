# to Add backslash quote and double quote in case to highklight something we use escape sequence charcacters

txt = "hello  we are the bloody 'peaky blinders' . how you are"
print(txt)

txt1 = "hello 'iam jawad' \"Nice to meet you\""
print(txt1)


# for printing words in new line use \n


txt2 = "yes \nits \ntooo \nhottttttttt"
print(txt2)


# \n is use for carriage return it take the cursor to the begining of new line

txt3 = "yes \rits \rtooo \rhottttttttt"
print(txt3)

# there are also alot of different methods
a = "brother"
b = "BROTHER"
# capitalize()	Converts the first character to upper case. 

print(a.capitalize())

# casefold()	Converts string into lower case

print(b.casefold())

# center()	Returns a centered stringlue occurs in a string
print(b.center(90))
# encode()	Returns an encoded version of the string
print(a.encode())
# count()	Returns the number of times a specified value occurs in string
print(a.count("r"))

# endswith()	Returns true if the string ends with the specified value
print(a.endswith("r"))
# expandtabs()	Sets the tab size of the string
print(b.expandtabs())

# find()	Searches the string for a specified value and returns the position of where it was found
print(a.find("t"))
# format()	Formats specified values in a string we did above


# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
j = "jack"
print(j.swapcase())