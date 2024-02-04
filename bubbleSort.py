def bubbleSort(list):
    n=len(list)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list=[12,6,7,4,56]
print(bubbleSort(list))