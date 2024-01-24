# calculate expances using function *********************(1)

def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total
tom_expances=[200,670,120,890]
joe_expances=[560,900,400,320]
tom_total=calculate_total(tom_expances)
joe_total=calculate_total(joe_expances)
print("tom's total expances is",tom_total)
print("joe's total expances is",joe_total)

# sum of two number using function

def sum(num1,num2):
    total=num1+num2
    return total
num1=int(input("enter the first number "))
num2=int(input("enter the second number "))
sum1=sum(num1,num2)
print("the sum of ",num1,"and",num2,"is",int(sum1))


#  Arguments in python are two types
# ******** NAMED ARGUMENTS
# ******** POSITIONAL ARGUMENTS