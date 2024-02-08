def fibonacci(num):
    fib=[0,1]
    while len(fib)<num:
        fib.append(fib[-1]+fib[-2])
    return fib
num=int (input("enter the number"))
print(fibonacci(num))