from numpy import *

arr1=array([
                [1,2,3,4],
                [5,6,7,8]
            ])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

m1=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2=matrix('9 8 7 ; 6 5 4 ; 3 2 1')

m3=m1 * m2

print(m3)