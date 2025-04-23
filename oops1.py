#Create 3 class with objects using oops concepts in python
class Vehicle:
    def __init__(self,type,color):
        self.type=type
        self.color=color
    def about(self):
        return f"This is a {self.type} which is in {self.color}"
model=Vehicle("car","black")
print(model.about())



class Animal():
    species="charlie"              #class variable
    def __init__(self,name,age):
        self.name=name             #instance variable       
        self.age=age
dog=Animal('Dog',10)               #instance properties
print(dog.name,dog.age,dog.species)



class Being():
    species1="human"
    species2="primate"
    def __init__(self,name,century):
        self.name=name
        self.cent=century
man=Being('Ajay',20)
monkey=Being('char',15)
print(man.name,man.cent,man.species1)
print(monkey.name,monkey.cent,monkey.species2)
man.name='Balu'
print(man.name,man.cent,man.species1)
Being.species1="humanbeing"
print(man.name,man.cent,man.species1)
