# polymorphism = creation of a structure or method that can be used with multiple objects or entities

class Ferrari():
    def speed(self):
        print("Ferrari: 349 km/h")

class McLaren():
    def speed(self):
        print("McLaren: 362 km/h")

def printSpeed(carType):
    carType.speed()

f = Ferrari()
m = McLaren()

printSpeed(f)
printSpeed(m)


