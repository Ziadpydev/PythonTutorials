from array import *

arr = array('i',[])

l = int(input("How Many Values You Need?"))

for i in range(l):
    x = int(input("Enter a number"))
    arr.append(x)

for e in arr:
    print(e)

i=0
j=l

while i<l and j>0:
    arr[i]=arr[j]
    i+=1
    j-=1

for e in arr:
    print(e)



