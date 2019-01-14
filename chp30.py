def person(name,age=18):
    print(name)
    print(age)

def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)

person('Zaid',27)
person(age=27,name='Zaid')
person('Zaid')

sum(5,6,12,34)