# pyramid - number pattern

a = int(input("Enter a value: "))
k=1
p=1
for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,k+1):
        print(p,end="")
    print()
    k=k+2
    p=p+2

