
def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)


person('Zaid',age=27,city='Pune',mob=9762868639)