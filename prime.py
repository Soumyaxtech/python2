def is_prime(num):
    if num<2:
        return False
    else :
        for i in range(2,int(num**0.5)+1):
           if num % i ==0:
            return False
        return True

def is_squreRoot_prime(num):
    squreRoot=int(num**0.5)
    return is_prime(squreRoot)
num=int(input("enter the number "))
if is_squreRoot_prime(num):
    print(num,"squre root is prime number")
else:
    print(num, "squre root is not prime number")