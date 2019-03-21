#working with Inheritance

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def displayName(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):  #Employee constructor
        Person.__init__(self,first, last)   #calling the Person constructor
        self.staffnumber = staffnum  #adding extra feature here

    def GetEmployee(self):
        return self.displayName() + ", " +  self.staffnumber
    
class PartTimeEmployee(Employee):
    
    def __init__(self,first,last,salary): 
        Employee.__init__(self,first,last)  
        self.EmpSalary=salary
        
    def GetPartTimeEmp(self):
        return self.displayName()+ " " +self.EmpSalary
        
            

P = Person("Marge", "Simpson")
E = Employee("Homer", "Simpson", "1007")
PE = PartTimeEmployee("Alok","Tripathi","50000")

print(P.displayName())
print(E.GetEmployee()) 
print(PE.GetPartTimeEmp()) 
