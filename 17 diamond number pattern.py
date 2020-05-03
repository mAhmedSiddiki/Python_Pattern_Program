# diamond - number pattern

a = int(input("Enter a value: "))

for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()

for i in range((a-1),0,-1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()


'''
OUTPUT:
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 
 4 4 4 4 
  3 3 3 
   2 2 
    1 
'''



for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range((a-1),0,-1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
    

'''
OUTPUT:
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 
 1 2 3 4 
  1 2 3 
   1 2 
    1 
'''