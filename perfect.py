def perfect(num):
    sum=0
    k=num
    if num<0:
        return False
    else:
        for i in range(1,k):
            if k%i==0:
                sum=sum+i

        if sum==num:
            return num

num=int(input("enter the number "))
if perfect(num):
    print(num,"is perfect number ")
else:
    print(num, "is not perfect number ")