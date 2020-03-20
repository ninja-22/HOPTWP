#!/usr/local/bin/python

class Id_Generator():
        def __init__(self):
                self.id = 0

        def generate(self):
                self.id = self.id + 1
                return self.id

class Employee():
        def __init__(self, Name, id_gen):
                self.Name = Name
                self.D_id = None
                self.Salary = None

        def printDetails(self):
                print("Employee Details: ")
                print(f"ID: {self.D_id}")
                print(f"Name: {self.Name}")
                print(f"Salary: {self.Salary}")
                print("-------------------------------------------------")

class Programmer():
        def __init__(self, name, id_gen, lang = None,
                db = None, projects = None, **add_skills):
                self.D_id = None
                self.languages = lang
                self.db = db
                self.projects = projects
                self.add_skills = add_skills
                super().__init__(name, id_gen)

        def printSkillDetails(self):
                print(f"ID: {self.D_id}")
                print(f"Languages: {self.languages}")
                print(f"Databases: {self.db}")



emp1 = Employee("Uthman", Id_Generator)
emp1.Salary = "£70,000"
emp1.D_id = 1
emp1.printDetails()

emp2 = Employee("Test", Id_Generator)
emp2.Salary = "£25,000"
emp2.D_id = 2
emp2.printDetails()
