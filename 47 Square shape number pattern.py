# square shape number pattern

a = int(input("Enter a value: "))

for row in range(0,a):
    for col in range(0,a):
        if(col==0 or col==(a-1)or((row==0 or row==(a-1))and(col>0 and col<(a-1)))):
            print("1 ",end="")
        else:
            print("0 ",end="")
    print()

