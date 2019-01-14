i = 1

while i<=5:
    j = 1
    print("Zaid ", end="")
    while j<=4:
        print("Rocks ", end="")
        j = j+1
    i = i+1
    print()

i=1
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)


i=1
print("Perfect Squares")
for i in range(1,501):
    if(i**2<=500):
        print(i**2)
    else:
        break