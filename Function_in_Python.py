
print(''' Functions in Python!!!
-------------------------------------------------------------------------''')
#you cannt call this here befor function definition!!!
#printMessage()

#def printMessage():
#    print("Hello I'm Python!!!  please define me befor use!  hah")
#    return

#printMessage()
empList = ['Tom','Sara','Mike']

def employeeAppend():   
    newEmp = input("Enter the Employee Name to Add:\t")
    empList.append(newEmp)
    print(empList[-1]+" Added Successfully!!")

def showEmployee():
    print("Showing the Employee list:\n")
    for emp in empList:
        print(emp)


        #calling the function
employeeAppend()
print("------------------------------------------------")
showEmployee()