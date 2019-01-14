#chp 42 43 44

class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        #print("Initialize")


    def config(self):
        print(self.cpu, self.ram, "1TB")

com1 = Computer('i5',16)
com2 = Computer('i7',32)
print(type(com1))
com1.config()
Computer.config(com2)

