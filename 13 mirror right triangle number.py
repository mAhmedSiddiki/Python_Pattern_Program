#mirror right triangle - number

a = int (input("Enter a value: "))

for i in range(0,a):
    print(" "*(a-i-1),end="")
    for j in range(0,i+1):
        print(j+1,end="")
    print()
'''
OUTPUT:
     1
    12
   123
  1234
 12345
'''



for i in range(0,a):
    print(" "*(a-i-1),end="")
    for j in range(0,i+1):
        print(i+1,end="")
    print()
    
'''
OUTPUT
    1
   22
  333
 4444
55555
'''