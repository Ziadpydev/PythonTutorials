
class Students:

    school="My School"              #Class Variable
    def __init__(self,m1,m2,m3):
        self.m1=m1                  #Instance Variable
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):           #Accessor Instance
        return self.m1

    def set_m1(self,value):     #Mutator Instance
        self.m1=value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student Static Class")


s1=Students(34,45,38)
s2=Students(25,42,40)

print(s1.avg())
print(s2.avg())

print(Students.getSchool())
Students.info()