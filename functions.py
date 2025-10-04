#functions are blocks of reusable blocks of code that perform specific task
#built in functions eg len(), max()
#user defined functions..created based on user needs and requirement
#lambda functions Anonymous functions defined using the lambda keyword
#some functions have default parameter values

# def name(names):#names is the parameter 
#     print("helo {names} is here")
# print(("matthew"))    




def add(a,b =5): #parameters acts a placeholders
    result = a + b
    return result
print(add(5,7))  
#the argument overrides the default value provided
## Functions return None by default when they have no return statement

#LAMBDA functions are small anonymous functions that can be defined by the lambda keyword ..usuaslly one liners 

#the function above can be written in the lambda form as 
add = lambda a, b: a-b
print(add(78,57))#no return keyword needed

print((lambda a, b: a - b)(3,4)) #no function name needed ..anonymous
