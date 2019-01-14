x=int(input("Enter a number "))
i=0

while i<=x:
    j=0
    while j<i:
        print("#",end="")
        j+=1
    i+=1
    print()

print()
i=0
while i<x:
    for j in range(x):
        print("$",end="")
    i+=1
    print()


print()
i=0
while i<x:
    for j in range(x-i):
        print(j+1,end="")
    i+=1
    print()
