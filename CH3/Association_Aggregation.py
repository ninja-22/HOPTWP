class Id_Generator():
    def __init__(self):
        self.id = 0

    def generate(self):
        self.id = self.id + 1
        return self.id

class Department():
    def __init__(self, name, location):
        self.name = name
        self.loc = location

    def DepartmentInfo(self):
        return f"Department Name: {self.name}, Location: {self.loc}"

class Manager():
    def __init__(self, m_id, name):
        self.m_id = m_id
        self.name = name

    def ManagerInfo(self):
        return f"Manager Name: {self.name}, Manager ID: {self.m_id}"

class Address():
    def __init__(self, country, state, area, street, zip_code):
        self.country = country
        self.state = state
        self.area = area
        self.street = street
        self.zip_code = zip_code

    def AddressInfo(self):
        return f"Country: {self.country}, State: {self.state}, Street: {self.street}"

class Employee():
    def __init__(self, Name, id_gen, dept = None, manager = None, address = None):
        self.Id = id_gen.generate()
        self.Name = Name
        self.D_id = None
        self.Salary = None
        self.dept = dept
        self.manager = manager
        self.address = address

    def PrintDetails(self):
        print("Employee Details: ")
        print(f"ID: {self.Id}")
        print(f"Name: {self.Name}")
        print(f"Salary: {self.Salary}")
        print(f"Department: \n\t{self.dept.DepartmentInfo()}")
        print(f"Manager: \n\t{self.manager.ManagerInfo()}")
        print(f"Address: \n\t{self.address.AddressInfo()}")

Id_gen = Id_Generator()
m = Manager(100, "Manager 1")
d = Department("IT", "London")
a = Address("UAE", "Dubai", "Al Jumeirah Rd", "xxxx 6", "xxxxx")
emp1 = Employee("Emp1", Id_gen, d, m, a)
emp1.Salary = 60000
emp1.D_id = 2
emp1.PrintDetails()