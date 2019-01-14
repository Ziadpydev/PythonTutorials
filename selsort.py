#Selection Sort

#Bubble Sort

def sort(nums):

    for i in range(len(nums)-1):
        min=i
        for j in range(i,len(nums)):
            if nums[j]<nums[min]:
                min=j

        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp
        print(nums)

list=[5,3,8,6,7,2]

sort(list)
print(list)
print(len(list))