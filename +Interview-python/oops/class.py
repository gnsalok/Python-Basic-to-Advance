'''
Instance Vs Class variable

Class variable - It could be access by the class and Instance as well.


'''

class Employee:
    no_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_emps += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.no_emps)



emp_1 = Employee('John', 'Son', 50000)
emp_2 = Employee('Jane', 'Son', 80000)

# print(emp_1.no_emps)

print(Employee.no_emps)

print(emp_1.fullname())
print(emp_1.email)
print(emp_1.pay)
print(emp_2.pay)

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)
print(emp_2.pay)
