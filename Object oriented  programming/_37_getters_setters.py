# getters in python are methods that are used 
# to access the value of an object properties they 
# are used to return the value of a specific
#  property and are typically defined using the @property decorator
# setters are used to set that value 

class Myclass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f" Value is {self.value}")    
    @property
    def value(self):
        return self._value           
   
    @value.setter
    def value(self, new_value):
        self._value = new_value



obj = Myclass(10)
obj.value = 80
print(obj.value)
obj.show()