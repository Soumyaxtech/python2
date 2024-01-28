str = "soumya"
str1 = str[1:-1]
print("the new string is ",str1)

#Take 2 strings, s1, and s2 return a new string made of the first, middle and last
#char of each input string

def com_str(str1,str2):
    str3=str1[0]+str1[int(len(str1)//2)]+str1[-1]+str2[0]+str2[int(len(str2)//2)]+str2[-1]
    return str3
str1=input("enter the 1st string")
str2=input("enter the 2nd string")
str4=com_str(str1,str2)
print(str4)

#Write a python program to take 2 strings, s1 and s2, create a new string by
#appending s2 in the middle of s1.

def new_str(str1,str2):
    str3=str1[:int(len(str1)//2)]+str2+str1[int(len(str1)//2):]
    return str3
str1=input("enter 1st string ")
str2=input("enter 2nd string ")
str4=new_str(str1,str2)
print(str4)
