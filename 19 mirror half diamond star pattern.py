# mirror half diamond star pattern

a = int(input("Enter a value: "))

for i in range(1,a+1):
    print(" "*(a-i)+"*"*i)

for i in range((a-1),0,-1):
    print(" "*(a-i)+"*"*i)

