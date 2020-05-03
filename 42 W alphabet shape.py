# W alphabet shape - star pattern

i=0#row
j=12#column
for row in range(0,5):
    for col in range(0,13):
        if(row==col or(row==3 and(col==5 or col==7))or(row==2 and col==6)):
            print("*",end="")
        elif(row==i and col==j):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(" ",end="")
    print()

