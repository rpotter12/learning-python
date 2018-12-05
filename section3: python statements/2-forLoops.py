# the term iterable means we can "iterate" over the object

# SYNTAX 
# my_iterable=[1,2,3,4,5]
# for item_name in my_iterable:
#     print(item_name)

mylist=[1,2,3,4,5]
for item in mylist:
    print(item)
# prints items of mylist

a=[(1,2),(3,4),(5,6)]
for item in a:
    print(item)
# print the list of tuples

for b,c in a:
    print(b)
    print(c)
# print all the elements in list separately

my_d={'a1':1 , 'a2':2}
for item in my_d.items():
    print(item)
# prints all dictionary items
