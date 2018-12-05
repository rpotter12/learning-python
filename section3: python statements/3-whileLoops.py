# while loops will continue to execute a block of code while some conditions remains true
# a while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition

# SYNTAX 
# while some_boolean_condition:
#     code

x=0
while x<5:
    print(f'x: {x}')
    x=x+1
# print the values 5 times
else:
    print('x is greater than 5')
print('\n\n')


# break - the break keyword stops the loop
# continue - the continue keyword goes to the top of the closest enclosing loop
# pass - does nothing

a=[1,2,3,4,5]
for item in a:
    pass
print("end")
