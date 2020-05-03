# double pyramid star pattern

a = int(input("Enter a value: "))

for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print("* ",end="")
    print(" "*((a-i)*2),end="")
    for k in range(1,i+1):
        print("* ",end="")
    print()

