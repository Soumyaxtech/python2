def vowel(str1):
    c=set("aeiouAEIOU")
    if set(str1)>=c:
        return "accepted"
    else:
        return "not accepted"
str1=input("enter the string ")
str2=vowel(str1)
print(str2)