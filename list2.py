list1=[12,34,12,78]
list2=[56,45,12,60]
list1.extend(list2)
print(list1)
list1.append(100)
print(list1)
list1.copy()
print(list1)
print(list1.count(12))
print(list1.index(34))
list1.insert(1,56)
print(list1)
list1.pop(2)
print(list1)
list1.remove(60)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list1.clear()
print(list1)