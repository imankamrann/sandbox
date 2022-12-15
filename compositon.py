class Car:
    def __init__(self, c):
        self.cartype = c
    
    def getCarType(self):
        return self.cartype
  

class Person:
    def __init__(self, n, a, c):
        self.name = n
        self.age = a
        self.car = c

    def displayPerson(self):
        print(f"{self.name} is {self.age} years old. she drives a {self.car.getCarType()}")
        
   
p = Person("marceline", 1000, Car("toyota"))
p.displayPerson()

b = Person("bubblegum", 830, Car("volks wagon"))
b.displayPerson()

