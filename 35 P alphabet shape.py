# P alphabet shape - star pattern

for row in range(0,7):
    for col in range(0,6):
        if(col==0 or (col==5 and (row==1 or row==2))or((row==0 or row==3)and(col>0 and col<5))):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

