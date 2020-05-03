# K alphabet shape - star pattern

for row in range(0,7):
    for col in range(0,5):
        if(col==0 or (col==1 and row==3)or((col==2)and(row==2 or row==4))or((col==3)and(row==1 or row==5))or((col==4)and(row==0 or row==6))):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

