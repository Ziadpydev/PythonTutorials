#Binary Search

pos=-1
def search(list,n):
    lb=0
    ub=len(list)-1
    while lb<=ub:
        mid=(lb+ub)//2
        if list[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]<n:
                lb=mid+1
            else:
                ub=mid-1

    return False

list=[4,7,8,12,45,99,112,365,485]
s=110

if search(list,s):
    print("Found at",pos+1)
else:
    print("Not Found")