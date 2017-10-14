#throwing an exception

#raise exception is used to raise the exception in python

value = 'Alok Tripathi'


def validateValue(value):
    if type(value)!=int:
        raise ValueError("Please enter correct value!")
    
    
    
#calling the function
validateValue(value)