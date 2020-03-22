
class ASP_Parent():
    def __init__(self, pub, prot, priv):
        self.public = pub
        self._protected = prot
        self.__private = priv

class ASP_child(ASP_Parent):
    def __init__(self, pub, prot, priv):
        super().__init__(pub, prot, priv)

    def printMembers(self):
        try:
            print(f"Public is: {self.public}")
            print(f"Protected is: {self._protected}")
            print(f"Private is: {self.__private}")
        except Exception as ex:
            print(f"Ex: {ex}")
            #pr = ASP_Parent()
            print(f"Private is: {self._ASP_Parent__private}")

ch = ASP_child(1, 2, 3)
ch.printMembers()
print(f"Public outside: {ch.public}")
print(f"Protected outside: {ch._protected}")
print(f"Private outside: {ch._ASP_Parent__private}")
