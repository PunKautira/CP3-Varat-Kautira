class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On: Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

PickUp1 = PickUp()
PickUp1.turnOnAirConditioner()


Van1 = Van()
Van1.turnOnAirConditioner()


EstateCar1 = EstateCar()
EstateCar1.turnOnAirConditioner()