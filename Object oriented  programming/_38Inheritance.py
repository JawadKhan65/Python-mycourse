# inheritance is like real world inheritance son can have his own specialities
# plus also from his father or parents
# same here is inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f" the name of Employee: {self.name}. Id : {self.id}")

# now lets make a  inherited class
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e = Employee("ROZE", 430)
e2 =Programmer("JOhn", 900)
e.showDetails( )
e2.showDetails()
e2.showLanguage()
# Programmer can use all methods of Employee but Employee cant
# ---------------------------------------------------------------
# by default access is public
# by using __ double underscore we cannot access it
# but can also access it with
# print(a._grape__name) this is called name mangling


class grape:
    def __init__(self):
        self._name = "hassan"
        self.__name = "hassan"
a = grape()
print(a._grape__name)        
print(a._name)        