# square number pattern

a = int(input("Enter a value: "))

for i in range(1,a+1):
    for j in range(1,a+1):
        print(i,end="")
    print()

'''
OUTPUT:
11111
22222
33333
44444
55555
'''



for i in range(1,a+1):
    for j in range(1,a+1):
        if(i==j):
            print("0",end="")
        else:
            print(i,end="")
    print()

'''
OUTPUT:
01111
20222
33033
44404
55550
'''
