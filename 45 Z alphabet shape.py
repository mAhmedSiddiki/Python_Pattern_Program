# Z alphabet shape - star pattern

i=1
j=3
for row in range(0,5):
    for col in range(0,5):
        if(row==0 or row==4):
            print("*",end="")
        elif(row==i and col==j):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(" ",end="")
    print()

