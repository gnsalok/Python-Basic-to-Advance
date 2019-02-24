# Working with Exception : Exception Handling ...

'''

try:    
    print(5/0)
    
except Exception as e: 
    print(e) 

finally:
    print("Finally block executed!!")

'''


try:
    value = int(input("Enter an integer value?"))

except Exception as e:
    print(e)

 # This will going to execute
finally:
    print("typecasting successfull")
