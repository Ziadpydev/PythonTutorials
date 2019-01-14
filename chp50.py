
class A:
    def __init__(self):
        print("In A init")

    def feat1(self):
        print("Feature 1A")

    def feat2(self):
        print("Feature 2")

class B:
    def __init__(self):
        print("In B init")

    def feat1(self):
        print("Feature 1B")

    def feat4(self):
        print("Feature 4")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")

    def feat5(self):
        print("Feature 5")


a=A()
b=B()
c=C()
c.feat1()