#chp 51 52 53 54

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyIDE:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=PyCharm()
ide1=MyIDE()
lap=Laptop()
lap.code(ide)
lap.code(ide1)