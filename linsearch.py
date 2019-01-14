
#Linear Search
pos=-1
def search(list,n):
    j=0
    #while i<len(list): #While Loop
     #   if list[i]==n:
      #      globals()['pos']=i
       #     return True
        #i+=1
    #return False

    for i in list:          #For Loop
        if i==n:
            globals()['pos']=j
            return True
        j+=1
    return False

list=[5,8,4,6,9,2]

s=4
if search(list,s):
    print("Found at",pos+1)
else:
    print("Not Found")