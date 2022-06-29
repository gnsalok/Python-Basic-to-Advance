class Employee:
    def __init__(self):
        self.name='Swati'
        self.salary=10000

    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)



emp = Employee()
print(emp)
