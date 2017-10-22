#data visualization with pandas

import pandas as pd

df=pd.read_csv('AirPassengers.csv')

print(df['AirPassengers'])

print(df['time'][135])

 
#Now we are trying to generate own CSV from the list of the data

EmployeeNames=['Alok','Amit','Aditya','Adarsh']
salary=[1000,2000,3000,4000]

data_set=list(zip(EmployeeNames,salary))

data_frame=pd.DataFrame(data=data_set, columns=['EmployeeName','Salary'])

data_frame.to_csv('emplObjFile.csv',index=True,header=True)

#Check you directory where you save your python file this would be generated 

