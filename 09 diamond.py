#diamond

a = int(input("Enter a value: "))

for i in range(0,a):
    print(" "*(a-i-1)+"* "*(i+1))

for j in range(a-1,0,-1):
    print(" "*(a-j)+"* "*(j))

