# pyramid - star pattern

a = int(input("Enter a value: "))#a=5

for i in range(1,a+1):
    for k in range(0,a-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()

