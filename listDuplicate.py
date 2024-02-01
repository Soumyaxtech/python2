def duplicate(list1):
    c=list(set(list1))
    return c

list1=[12,67,34,12,56,67,34,90]
list2=duplicate(list1)
print(list1)
print(list2)