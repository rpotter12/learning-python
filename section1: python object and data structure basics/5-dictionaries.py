# dictionaries are unordered mapping for storing objects.
# dictionaries use a key-value pairing
# this key-value pair allows user to quickly grab objects without needing to know an index location
# dictionaries use curly braces and colons to signify the keys and their associated values.
# SYNTAX: {'key1':'value1','key2':'value2'}

mydic={'name1':'abc','name2':'pqr'}
print(mydic)

# there is no need to use index position to get the value
print(mydic['name1']) #print value abc

# example: prices of items in store
print("\n\n")
# we put list as value
a={'k1':1,'k2':[2,3,4],'k3':{'k3_1':5}}
print(a['k2'])
print(a['k3']['k3_1'])

# to insert new value in dictionary
a['k4']=6
print(a)

print("\n\n")
# dictionaries is also having various methods
print(f"keys: {a.keys()}")
print(f"values: {a.values()}")
print(f"items: {a.items()}")

