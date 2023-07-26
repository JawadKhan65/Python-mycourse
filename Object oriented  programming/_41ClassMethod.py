class Bhai:
    company = "Apple"
    def show(self):
        print(f" the name is {self.name} andd company is {self.company}")
    @classmethod
    def Changecomapny(cls, newCompany):
        cls.company = newCompany

e1 = Bhai()
e1.name = "jawad"
e1.show() 
e1.Changecomapny("Google") 
e1.show()     
print(Bhai.company) #this will give apple but thats not true we changed the company
# but for changing company we have to use @classmethod so it can change it
# writig it above Chagecompany than it will show comapny as google
