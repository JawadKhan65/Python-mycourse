# static methods belong to class but the are not the instance of class 
class Math:
    def __init__(self, num):
        self.num = num
    def addtoNum(self, n):
        self.num = self.num + n
    @staticmethod
    def add(a, b):
        return a + b   


a = Math(5)
print(a.num)
a.addtoNum(6)
print(a.num)

# but with static method we dont need to make objects or no need to give self as argument
# you can call it by either by object or by class
print(Math.add(5, 6))
print(a.add(5, 6))



class GRoup:
    def __init__(self, num) :
        self.num = int(num)
    def table(self):
            for i in range(1, 11):
                 print(f"{self.num} X {i} = {self.num * i}")
    def table2(self):
            for i in range(1, 22):
                 print(f"{self.num} X {i+4} = {self.num * (i+4)}")
ab = GRoup(8)
ab.table() 
print("wait")
ab.table2()             