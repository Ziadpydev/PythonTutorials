#chp 34 35 36

import sys

sys.getrecursionlimit()
sys.setrecursionlimit(1500)

def fact(x):

    f=1
    for i in range(1,x+1):
       f=f*i
    return f

def fact1(x):
    if(x==0):
        return 1
    return x*fact1(x-1)

res=fact(4)
print(res)
res1=fact1(5)
print(res1)