#x = int(input("How Many Candies?"))
#i = 1
#candy = 20

#while i<=x:
#    if i>candy:
#        print("Insufficient Candy")
#        break
#    print(i,"Candy")
#    i+=1

#print()
#print("Numbers")
#for i in range(1,30):
#    if i%3==0 or i%5==0:
#        continue
#    print(i)

print("Fibonaci Series")
j=1
i=1
temp=0
for k in range(50):
    if k==0 or k==1:
        print(1)
    else:
        print(i+j)
        temp=i+j
        i=j
        j=temp
