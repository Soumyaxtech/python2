def print_tipsy_topsy(n):
    for i in range(11, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            print(i,"TipsyTopsy")
        elif i % 3 == 0:
            print(i,"Tipsy")
        elif i % 7 == 0:
            print(i,"Topsy")



N = int(input("Enter a number greater than 20 (N): "))
print_tipsy_topsy(N)