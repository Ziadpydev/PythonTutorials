
def greet():
    print("Hello")
    print("Good Morning")

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

greet()

res,res2=add_sub(4,5)
print(res,res2)