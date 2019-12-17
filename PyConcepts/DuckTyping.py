'''
Duck Typing : *  Quite simply put, Duck typing gives a programmer the ability to not worry about
the type of a class rather perform the required operations.
'''


class Duck:
    def quack(self):
        print("Quacked")


class AnotherDuck:
    def quack(self):
        print("Louder Quack")


class Eagle:
    def fly(self):
        print("Dude i just fly")



#Duck Typing implemantation is here 
class MakeItQuack:
    def __init__(self, bird):
        bird.quack()


MakeItQuack(Duck())
MakeItQuack(AnotherDuck())
MakeItQuack(Eagle())
