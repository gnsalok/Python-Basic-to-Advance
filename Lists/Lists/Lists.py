print(''' Let's working with the List
-----------------------------------------------------------''')


listEmployee=['TOM','BOB','SARA','JOHN']


#Loop through all the employee in list
for steps in range(0,4):
    print(listEmployee[steps])


listEmployee.append('Alok')
#Displaying last item in the list
#print(listEmployee[-1])
   

#Adding the employee in the list

listEmployee.remove('JOHN')

print(listEmployee[-1])


