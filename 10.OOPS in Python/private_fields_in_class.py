#Defining private fields inside the class 
#Implementing Encapsulation (i.e. Abstraction)

class Complex:
    'This class simulates the complex numbers'
    def __init__(self,real=0,imag=0):
        if(type(real) not in (int,float)) or type(imag) not in (int,float) :
            raise Exception('Arguments are not valid!')
        self.__real=real        #This is gonna to your private field  (__real)
        self.__imag=imag
    def getReal(self):
        return self.__real       
    def setReal(self,val):         
        self.__real=val           
    def setImag(self,val):
        self.__imag=val     
    def getImag(self):
        return self.__imag
        #defining the get and set method to access and define the private fields
        
        

#creating the Instance

C = Complex()
C.setReal(12)
print("Real Number is :",C.getReal())
    
C.setImag(15)
print("Imaginary Number is :",C.getImag())
    

     
    
'''
Exeptino Handling Syntax:-
try:
    #Statemetns
except Exception as e"
    #print the error message    
'''    
       

