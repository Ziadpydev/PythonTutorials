#chp 45

class Computer:
    def __init__(self):
        self.name = 'Zaid'
        self.age = 27

    def update(self):
        self.age=30

    def compare(self,other):
        if self.name == other.name:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
c1.age=29
c1.update()
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

if c1.compare(c2):
    print("They are Same")
else:
    print("They are not same")

