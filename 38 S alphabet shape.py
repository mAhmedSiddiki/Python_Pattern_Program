# S alphabet shape - star pattern

for row in range(0,9):
    for col in range(0,5):
        if((col==0 and ((row>0 and row<4)or row==7))or(col==4 and(row==1 or(row>4 and row<8)))or((row==0 or row==4 or row==8)and(col>0 and col<4))):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

