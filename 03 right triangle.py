#right- triangle

a = int(input("Enter a value: ")) #a=5

for i in range(1,a+1):
    k=i
    for j in range(1,i+k):
        print("* ",end="")
        k=2
    print()