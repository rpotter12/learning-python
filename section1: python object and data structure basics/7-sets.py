# sets are unordered collection of unique elements
# meaning there can only be one representative of the same object

my_set=set()
print(my_set) # returns empty set

# to insert value in set we can use 'variable.add(value)'
my_set.add(1)
my_set.add(2)
print(my_set) # returns {1,2}

# if we try add 2 again, it will not inset in it
my_set.add(2)
print(my_set) # returns {1,2}

# there are some difference in printing format in python2 and python3
