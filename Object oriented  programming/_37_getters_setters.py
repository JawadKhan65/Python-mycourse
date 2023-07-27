# getters in python are methods that are used 
# to access the value of an object properties they 
# are used to return the value of a specific
#  property and are typically defined using the @property decorator
# setters are used to set that value 

class Myclass:
    def __init__(self, value):
        self._value = value # _value is  to make it private
    def show(self):
        print(f" Value is {self._value}")    
    @property  # it is for making a getter 
    def tenvalue(self):
        return 10*self._value
   
    @tenvalue.setter # for setter
    def tenvalue(self, new_value):
        self._value = new_value/10



obj = Myclass(10)
# print(obj._value)s
obj.tenvalue = 67
print(obj.tenvalue)
obj.show()