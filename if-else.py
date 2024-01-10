 # # #    MAKEING A CALCULATOR USING IF-ELSE STATEMENT(MINI-PROJECT)

num1 = input("enter first number : ")
operation = input("enter your operation(+,-,*,/,//,%) : ")
num2 = input("enter second number : ")
num1 = int(num1)
num2 = int(num2)
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
elif operation == "//":
    print(num1 // num2)
elif operation == "%":
    print(num1 % num2)
else:
    print("invalid operation ")
