
class Car():

    wheels = 4                  #class Namespace
    def __init__(self,mil,com):
        self.mil = mil          #instance Namespace
        self.com = com          #instance Namespace

c1=Car(10,"BMW")
c2=Car(15,"Porsche")

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
c2.wheels=5                     #Only changes for this object
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
Car.wheels=8                    #changes for class so for all objects
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
