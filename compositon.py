class Car:
    def __init__(self, c):
        self.cartype = c
    
    def getCarType(self):
        return self.cartype
  


class Person:
    def __init__(self):
        self.car = Car("toyota")

    def displayPerson(self, a):
        print(f"marceline is {a} years old. she drives a {self.car.getCarType()}")
        
   
p = Person()
p.displayPerson(16)
