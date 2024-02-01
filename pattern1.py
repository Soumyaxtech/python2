rows=int(input("enter no of rows "))
for i in range(1,rows+1):
    k=[2**j for j in range(i)]
    print(*k[::-1])


