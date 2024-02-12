#functions in python
#like in mathematics, where a function takes an argument and produces a result, it does so in python as well
#the general forms of a python function is:
#def function name (arguments):
# {lines telling the function what to do to produce the result}
# return result

#lets consider producting a function that produces x^2
def squared(x, y):
    result = x**2 + y**2
    return result
print(squared(10,2))

#a new function
def born(country):
    return print("I am from " + country)

born("England")