def duplicate(str):
    c=set()
    result=[]
    for char in str:
        if char not in c:
            result.append(char)
            c.add(char)
    result_str=''.join (result)
    return result_str
str=input("enter the string ")
str1=duplicate(str)
print("input is ",str)
print("output is ",str1)