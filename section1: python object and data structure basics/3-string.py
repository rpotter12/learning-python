# strings are the sequence of characters, using the syntax of either single quotes or double quotes: 'hello' "hello" "I don't"

# slicing allow  you to grab a subsection of multiple characters, a slice of a string
# this has a following syntax: [start:stop:step]
# start is a numerical index for slice start
# stop is the index you will go up to (but not include)
# step is the size of the jump you take.
# use + sign for concatenation
# string has inbuilt functions. use that function with the help of . operator
# .format() is used in print function to print variable with a string

a='string'
print(a)

a="i am"
print(a)

print("hello \n world")

print(len(a))

a="hi my name is hello world"
print(a[10])
print(a[12])

mystring="abcdefghijk"
print(mystring[3])
print(mystring[2:])
print(mystring[:3])
print(mystring[3:6])
print(mystring[::])
print(mystring[::2])
print(mystring[2:7:2])

print("\n\n")

x="hello world"
print(x+" it is beatiful world outside")

print("\n\n")

ab='z'
print(ab*10) # this will print z 10 times

print("\n\n")

x="hello python"
print(x.upper())

print("\n\n")

print('this is a string {}'.format('INSERTED'))

print(f'hi {x}') # if you are using this type, use python3 to run the code
