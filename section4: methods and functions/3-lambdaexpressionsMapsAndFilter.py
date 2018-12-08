# lambda expressions - lambda operator or lambda function is used for creating small, one-time and anonymous function objects in Python. Basic syntax lambda arguments : expression. lambda operator can have any number of arguments, but it can have only one expression
# map - map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# filter - The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

## MAP ##
def square(num):
    return num**2
my_nums=[1,2,3,4,5]
for item in map(square,my_nums):
    print(item)

# or #
list(map(square,my_nums))

## FILTER ##
def check_even(num):
    return num%2==0
mynums=[1,2,3,4,5,6,7]
list(filter(check_even,mynums))

## LAMBDA ##
squar=lambda num: num ** 2
square(5)

list(map(lambda num:num**2,mynums))
