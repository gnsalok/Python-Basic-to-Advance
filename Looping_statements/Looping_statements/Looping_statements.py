
import turtle

#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)

#for steps in range(4):
#    turtle.color('red')
#    turtle.forward(100)
#    turtle.color('blue')
#    turtle.right(90)
#    turtle.color('green')
#    turtle.speed(1)
    #just wow


#Acces the value of the loop
    
#its runs 3 time cause starts from 1
for steps in range(1,4):
    print("Hello Alok")
     
 #steps contains the value starting from value you start the loop 
 # range(start, range)   
for steps in range(1,4):
    print(steps)

    #here range(start, stop, range)
for steps in range(1,2,4):
    print(steps)
    

    
for steps in ['red','blue','green','yellow']:
    turtle.color(steps)     #what a feature !!
    turtle.forward(200)   
    turtle.left(90)
    #if steps == 'yellow' :
    #    turtle.forward(100)
    #    turtle.right(90)
    

    turtle.speed(1)
