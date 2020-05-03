# T alphabet shape - star pattern

for row in range(0,6):
    for col in range(0,5):
        if(row==0 or (col==2 and (row>0 and row<6))):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

