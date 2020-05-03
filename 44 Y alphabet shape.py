# Y alphabet shape - star pattern

i=0#row
j=6#column
for row in range(0,7):
    for col in range(0,7):
        if((row==col and col<3)or(col==3 and (row>2 and row<7))):
            print("*",end="")
        elif(row==i and col==j):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(" ",end="")
    print()

