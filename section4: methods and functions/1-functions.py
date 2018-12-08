# A function in Python is defined by a def statement. 
# The general syntax looks like this: def function-name(Parameter list): statements, i.e. the function body. 
# The parameter list consists of none or more parameters. 
# Parameters are called arguments, if the function is called.
# functions allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire block of code


# SYNTAX-     
# def name_of_function():
#     commands

# we use the return keyword to send back the result of the function, instead of just printing it out.
# return allow us to assign the output of the function to a new variable.

def abc():
    print('hello world')

def sum(a,b):
    return a+b


abc() 
print(sum(5,6))
