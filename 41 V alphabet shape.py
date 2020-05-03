# V alphabet shape - star pattern

for row in range(0,4):
    for col in range(0,7):
        if(row==col or(row==0 and col==6)or(row==1 and col==5)or(row==2 and col==4)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

