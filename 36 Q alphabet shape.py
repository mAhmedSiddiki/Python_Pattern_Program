# Q alphabet shape - star pattern

for row in range(0,8):
    for col in range(0,6):
        if(((row==0 or row==5)and(col>0 and col<4))or((col==0)and(row>0 and row<5))or(col==4 and(row!=0 and row!=5 and row!=7))or(row==7 and col==5)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

