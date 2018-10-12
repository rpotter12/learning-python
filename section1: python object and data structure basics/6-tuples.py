# tuples are very similar to lists.
# they have one key difference - immutability
# that means if an element is inside a tuple, it can't be reassigned.
# tuples use parenthesis: (1,2,3)
# tuples have very less function - .index() , .count()

my_tuple=(1,2,3)
print(my_tuple) # prints all element in my_tuple

print("\n\n")

# in tuples we can also use multiple data types as elements
t=('name',1,1.28)
print(t)


# indexing and slicing can also be done in tuple
print(t[0])

print("\n\n")

# functions in tuples
t=('a','a','a','b','c')
print(t.count('a')) # returns value 3, a is present 3 times in tulpe t
print(t.index('b')) # returns value 3, b is present at 3 index
