def is_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
def print_prime(n):
    for i in range(0,int(n+1)):
        if is_prime(i):
            print(i,"")
n=int (input("enter the range"))
print_prime(n)
