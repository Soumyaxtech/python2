def divisible(n,m):
    for i in range(1,n+1):
        if i%m==0:
            print(i,"is divisible by",m)
            if i%2==0:
                print(i,"is even number ")
            else:
                print(i,"is odd number ")
n=int(input("enter the range "))
m=int (input("enter num "))
k=divisible(n,m)
print(k)