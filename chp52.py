
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def  __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3

    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        print(m1,m2)
        if m1>m2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2) #it returns tuple so formatted to return string

s1=Student(58,69)
s2=Student(80,65)

s3=s1+s2                        #Student.__add__(s1,s2) inbuilt functions
print(s3.m1,s3.m2)

if s1>s2:
    print("S1 wins")
else:
    print("S2 wins")

print(s1)                       #str.__str__(s1) inbuilt functions
print(s2)