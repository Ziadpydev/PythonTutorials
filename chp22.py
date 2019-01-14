
from array import *

vals = array('i',[5,9,8,-4,2])
print(vals)
vals=sorted(vals,key=int)
print(vals)
#print(vals.buffer_info())
vals.append(35)

for i in range(len(vals)):
    print(vals[i])
vals.reverse()
for e in vals:
    print(e)

#newArr = array(vals.typecode,(a for a in vals))
#print(newArr)


