class Car():
    def __init__(self, cat, mil, cap):
        self.category = cat
        self.mileage = mil
        self.capacity = cap


class Ferrari(Car):
    def __init__(self, cat, mil, cap, HP, TS, ACC):
        super().__init__(cat, mil, cap)                 # have to declare this super() statement to ensure that the Ferrari class can access the variables already defined in the Car class - this is not automatic or implicit
        self.HorsePower = HP
        self.TopSpeed = TS
        self.Acceleration = ACC

    def printCarDetails(self):
        engine = Engine()
        print(f"Category: {self.category}")
        print(f"Mileage: {self.mileage}")
        print(f"Capacity: {self.capacity}")
        print(f"Horse Power: {self.HorsePower}")
        print(f"Top Speed: {self.TopSpeed}")
        print(f"Acceleration: {self.Acceleration}")
        print(f"Engine: ")
        print(f"\t" + (engine.Details()))

class Engine():
    def __init__(self):
        self.details = None

    def Details(self):
        self.details = """
        The 450 is powered by blah blah blah """
        return self.details

obj = Ferrari("Sports", "4kmph", "4 seater", "660 horsepower", "349 km/h", "2.9s")
obj.printCarDetails()


