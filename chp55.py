
a=5
b=0

try:
    print("Resource Opened")
    print(a/b)
except Exception as e:
    print("Error: ",e)
finally:
    print("Resource Closed")

print("Bye")