# Working with Lambda Functions...

'''
-> lambda operator are useful when you have need to implemnt function in order to inline.

->lambda is just like Ananymous Fuction, a function without name means function having 
definition not the implementation.

'''
#Declare and define the function
addValues = lambda num1,num2 :num1+num2

#calling the function
print
("Sum is :",addValues(12,13))  #results 25


# Its very helpful when you write nesting of the function

'''

resultMult = lambda a : lambda b : lambda c : a*b*c

print(resultMult(5)(2)(5)) # Reslults 50

'''


getName = lambda  name : name


print(getName('Alok'))