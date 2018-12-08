# *args - arguments  - it returns tuple
# **kwargs - keyword arguments - it returns dictionary


def myfunc(*args):
    print(args)
myfunc(1,2,3,4,5,6,7,8,9,0)


def myfunc1(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
myfunc1(fruit='apple',veggie='lettuce')
