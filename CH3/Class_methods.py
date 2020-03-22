class Methods():
    class_var = 200
    def __init__(self):
        self.variable = 0

    def instance_method(self):
        self.variable = 100
        print("-----------------------------------------")
        print("Inside Instance Method")
        print(f"Instance is: {self}")
        print(f"Instance variable is: {self.variable}")
        print(f"Class variable is: {self.__class__.class_var}")
        print("-----------------------------------------")

    @classmethod
    def class_method(cls):
        print("-----------------------------------------")
        print("Inside Class Method")
        try:
            self.variable = 22
            print(f"Instance variable is: {Methods().variable}")
        except Exception as ex:
            print("Can't access instance variable in class method")

        cls.class_var = 33
        print(f"Class is: {cls}")
        print(f"Class variable is: {cls.class_var}")
        print("-----------------------------------------")


    @staticmethod
    def static_method():
        print("Inside Static Method")
        try:
            print(f"Class = {class_var} and Instance = {self.variable}")
        except Exception as ex:
            print("Cannot access class and instance variable in static method")

class Driver():
    def main(self):
        o = Methods()
        o.instance_method()
        o.class_method()
        Methods.class_method()
        o.static_method()
        Methods.static_method()
        print("Let's see variable access of class variables \n\n")
        print("-----------------------------------------")
        print(f"Accessing class variables with Instance o: {o.class_var}")
        o.class_var = 222
        print("Modifying class variable with Instance o: o.class_var = 222")
        print(f"Accessing modified class variable with Instance o: {o.class_var}")
        print("-----------------------------------------\n\n")
        print("-----------------------------------------")
        oo = Methods()
        print(f"Accessing class variables with Instance oo: {oo.class_var}")
        print("Changes not persisted thus modifying o.class_var created local copy for instance o")
        print("-----------------------------------------\n\n")
        print("-----------------------------------------")
        print(f"Accessing class variables with Class variable: {Methods.class_var}")
        print("Changes not persisted thus modifying o.class_var created local copy for instance o")
        print("-----------------------------------------\n\n")
        print("-----------------------------------------")

d = Driver(); d.main()


