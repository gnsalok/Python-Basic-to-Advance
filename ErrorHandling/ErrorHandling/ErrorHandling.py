print(''' Error Handling 
---------''')

num=int(input("Enter your numerator?"))
den=int(input("Enter your denominator?"))

try:
    
        divResult=num/den

except Exception as e:
    print(''' There is an Exception Occure
    -------------Exception is ----------------------''')
    print(e)

finally:
    print('Finally block is executed')
    





