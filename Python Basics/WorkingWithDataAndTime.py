#Think what happens here..
print('''Working with Date and Time
---------------------------------------------------
''')


#import the name space
import datetime

print(datetime.date.today())

#this shows you all the libraries
#print(dir(__build_class__))


currentDate=datetime.date.today()

print(currentDate)
print(currentDate.month)
print(currentDate.year)
#let's formate the time
print(currentDate.strftime('%d %b %Y'))


print('''
------------------------------''')
print("Working with Time Now!!!")
print("--------------------------------------------------")


currentTime=datetime.datetime.now()
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)


