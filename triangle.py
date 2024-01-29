def triangle(s1,s2,s3):
    if s1+s2<=s3 or s1+s3<=s2 or s2+s3<=s1:
        return "not a triangle"
    elif s1==s2==s3:
        return "Equilateral"
    elif s1 == s2 or s1 == s3 or s2 == s3:
        return "Isosceles"
    else:
        return "Scalene"
s1=int(input("enter 1st length "))
s2=int(input("enter 2nd length "))
s3=int(input("enter 3rd length "))
s4=triangle(s1,s2,s3)
print(s4)
