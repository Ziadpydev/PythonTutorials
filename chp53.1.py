
class A:
    def show(self):
        print("In A Show")

class B(A):
    def show(self):
        print("In B Show")

a=B()
a.show()