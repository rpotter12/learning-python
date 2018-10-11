# list are ordered sequence that can hold a variety of object types
# they use [] brackets and commas to separate objects in the list. eg- [1,2,3,4,5]
# list support indexing and slicing
# list can be nested and also have a variety of useful method that can be called off of them.

my_list=[1,2,3,4,5]
print(my_list)
print("\n\n")

my_list=["name",1,1.23]
print(len(my_list))
print(my_list)

my_list=[1,2,3,4,5]
# indexing and slicing
print(my_list[0])
print(my_list[1:])

# concatenation
my_list2=[6,7]
my_list=my_list+my_list2
print(my_list)

# list have various methods. append() method add element at the last
my_list.append(8)
print(my_list)
print("\n\n")

# pop() method is to delete element
print(f"popped element: {my_list.pop()}") #delete the last element
print(my_list)
print(f"popped element at particular position: {my_list.pop(0)}")

# sort() method sort the list
# reverse() method reverse the order of the list
