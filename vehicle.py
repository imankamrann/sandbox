class Vehicle:
    def __init__(self, started, speed):
        self.started = True
        self.speed = speed
    def start(self):
        pass
    def increase_speed(delta):
        pass

class Car(Vehicle):
    def __init__(self, trunk_open):
        super().__init__(trunk_open)
        self.trunk_open = True
    def open_trunk():
        pass
    def close_trunk():
        pass


class Motorcycle(Vehicle):
    def __init__(self, center_stand_out):
        super().__init__(center_stand_out)
        self.center_stand_out = True
   