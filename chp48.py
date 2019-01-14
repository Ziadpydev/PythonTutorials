
class Student:

    def __init__(self,name,roll,brand,cpu,ram):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop(brand,cpu,ram)     #Instance of inner class created

    def show(self):
        print("Name:",self.name,"Roll No:",self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def show(self):
            print("Brand Name:", self.brand, "CPU:", self.cpu, "RAM:", self.ram)

s1=Student('Zaid',471,'HP','i5','8GB')
s2=Student('Khan',145,'Lenovo','i3','12GB')
s1.show()
s1.lap.show()               #Calling inner class method using outer class and inner class object
s2.show()
s3=Student.Laptop('Samsung','i7','16GB')
s3.show()                   #External Creation of object for inner class