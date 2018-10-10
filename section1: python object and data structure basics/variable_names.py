# rules for variable names:
# 1. name cannot start with a number
# 2. there can be no spaces in the name, use _ instead
# 3. can't use any of the symbols:  !@#$%^&*()-+~<>,'
# 4. it's considered best practice (PEP8) that names are lowercase
# 5. avoid using word words that have special meaning in python like "list" and "str"

# python allow DYNAMIC TYPING: means we can reassign variable to different data type
# use type() to know the data type of the variable

a=5
print(a)
print(type(a))

a=10
print(a)
print(type(a))

a=a*a
print(a)
print(type(a))

a="name"
print(a)
print(type(a))
