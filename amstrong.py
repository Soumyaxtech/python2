def amstrong(num):
    k=num
    sum=0
    str1=str(num)
    digit=len(str1)
    while k>0:
        rem=k%10
        k=k//10
        sum=sum+rem**digit

    if sum==num:
        return num
num=int(input("enter a number "))
if amstrong(num):
    print(num,"is a amstrong number")
else:
    print(num,"is not a amstrong number")
