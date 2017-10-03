#Challenge : traverse the string using for loop

stringValue = "Hey Python Geeks!"

'''
# 1st way
for steps in range(len(stringValue)):
    print(stringValue[steps])
    
    
#2nd way

for char in stringValue:
    print(char)
    
  '''  
    
#Nesting of for loop
    
for i in range(1,4):   
    for j in range(1,5):
        print('{:<2} '.format(i*j),end="")