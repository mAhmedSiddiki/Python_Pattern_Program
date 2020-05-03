# U alphabet shape - star pattern

for row in range(0,6):
    for col in range(0,5):
        if(((col==0 or col==4)and(row!=5))or(row==5 and(col>0 and col<4))):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

