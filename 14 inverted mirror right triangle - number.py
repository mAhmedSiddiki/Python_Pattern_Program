# inverted mirror right triangle - number

a = int(input("Enter a value: "))

for i in range(a+1,1,-1):
    print(" "*(a+1-i),end="")
    for j in range(1,i):
        print(j,end="")
    print()
    
    
'''
OUTPUT:
12345
 1234
  123
   12
    1
'''




for i in range(a+1,1,-1):
    print(" "*(a+1-i),end="")
    for j in range(1,i):
        print(i-1,end="")
    print()


'''
OUTPUT:
55555
 4444
  333
   22
    1
'''