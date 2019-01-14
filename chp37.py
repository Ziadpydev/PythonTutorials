#37 38

from functools import reduce

f= lambda a : a*a
res= f(5)
print(res)


nums=[3,2,6,8,4,5,7,12,11]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
doubles=list(map(lambda n:n*2,evens))
print(doubles)
sum=reduce(lambda a,b:a+b,doubles)
print(sum)