#Nesting of the function 

# Note that you have to use ; for the nested function



def outerFunction(a):
    def innerFunction(b):
        return a*b;              #semi-colon is here..
    return innerFunction


print(outerFunction(5)(5))