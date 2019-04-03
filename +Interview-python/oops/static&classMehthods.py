'''
static vs class methods vs instance method

Static Method -- They behave just like normal functions,
yet they should have some logical connection to our class

'''


class Employee:
    empCount=0          #class variable
       
    def __init__(self):             #Instance method with first arg as self
        Employee.empCount+=1        #calling with class name

    @classmethod                     #Class method with first arg as cls
    def classMethod(cls):
        pass    

    @staticmethod                    #static method no args 
    def isWorkday(day):               # if there is some method hv logical connection 
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True


import datetime

E1=Employee()
print(E1.empCount)



print(Employee.empCount)

my_date = datetime.date(2019,7,22)         
print(Employee.isWorkday(my_date))


print(Employee.__dict__)


E1.is