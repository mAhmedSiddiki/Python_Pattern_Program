# inverted mirror right triangle

a = int(input("Enter a value: "))#a=5

for i in range(a,0,-1):
    s=i-1
    for j in range(0,i):
        print("*",end="")
    print()
    for k in range(0,a-s):
        print(" ",end="")
