class Car:
    def __init__(self,c):
        self.cartype = "toyota"

    def sounds(self):
        print("vroom vroom!")



class Person:
    def __init__(self, a, c):
        self.a = a
        self.car = Car(c)

    def displayPerson(self,a,):
        print(f"marceline is {a} years old. she drives a {self.car}")
        Car().sounds
   
p = Person(16)
p.displayPerson
