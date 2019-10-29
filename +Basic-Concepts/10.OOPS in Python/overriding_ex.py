class Animal:
   def __init__(self):
       print("Animal Constructor")
       self.age = 1 


#Inheritance 
class Mammel(Animal):
   def __init__(self):
       print("Mammel Constructor")
       #Mehthod overriding
       self.weight=2
       #This will execute Animal constructor in last 
       super().__init__() 
    



m = Mammel()
print(m.age)
print(m.weight)