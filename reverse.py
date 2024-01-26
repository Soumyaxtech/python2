def reverse(num):
    sum=0
    i=num
    while i> 0 :
        rem=i%10
        i=i//10
        sum=sum*10+rem
    return sum
def even(num):
    return(num%2==0)
num=int(input("enter a number "))
sum1=reverse(num)
print(sum1)
if even(num):
    print(num,"is even number")
else:
    print(num,"is odd number")
