# hollow diamond - star pattern

for row in range(0,9):
    for col in range(0,9):
        if(row+col==4 or col-row==4 or row-col==4 or row+col==12):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

