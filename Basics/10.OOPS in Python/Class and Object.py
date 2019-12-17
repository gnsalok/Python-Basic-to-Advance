#Working with classes and object..

class Complex:
    'This class simulates the complex numbers'
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

C=Complex(12,15)    
print(C.real, C.imag)


'''
##Test Yourself
#class Employee:  
#    Name=""
#    Id=""
#    def __init__(self,name,id):
#        self.Name=name  #self in used as this in another language like C#,Java and javascript
#        self.Id=id
#        
#    def showEmployee(self): #This is gonna to class Method or action
#        print("Name is {0} and ID is: {1}  ".format(self.Name,self.Id))
#        
#E=Employee("Alok Tripathi" , 1)
#E.showEmployee()

'''