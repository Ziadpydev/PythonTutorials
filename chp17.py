x=int(input("Enter a number"))

if x>0:
    print("Positive")
else:
    print("Negative")

p = int(input("Enter a number"))
q = int(input("Enter a number"))
r = int(input("Enter a number"))

if p>q and p>r:
    print(p, "Greater")
elif q>p and q>r:
    print(q, "Greater")
else:
    print(r, "Greater")