#inverted pyramid

a = int(input("Enter a value: "))

for i in range(a,0,-1):
    for k in range(0,a-i):
        print(" ",end="")
    for j in range(0,i):
        print("* ",end="")
    print()