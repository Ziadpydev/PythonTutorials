
class A:
    def feat1(self):
        print("Feature 1")

    def feat2(self):
        print("Feature 2")

class B(A):
    def feat3(self):
        print("Feature 3")

    def feat4(self):
        print("Feature 4")

class D:
    def featD(self):
        print("Feature D")

class C(B,D):
    def feat5(self):
        print("Feature 5")


a1=A()
a1.feat1()
a1.feat2()

print("SingleLevel Inheritence")
b1=B()
b1.feat1()
b1.feat2()
b1.feat3()
b1.feat4()

print("MultiLevel Inheritence")
c1=C()
c1.feat1()
c1.feat2()
c1.feat3()
c1.feat4()
c1.feat5()
print("Multiple Inheritence")
c1.featD()