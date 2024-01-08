name = input("enter a string ")
# DIFF STRING OPERATIONS**************
print(name.upper())  # uppercase
print(name.lower())  # lowercase
val = input("what letter you want to find ")
print(name.find(val))  # it will give you the index of the letter if present
name1 = input("enter string to replace ")
print(name.replace(name,name1))  # it will replace the string
val1= input("what letter you want to find ")
print("val1" in name)  # it will return true or false
print(name)
print(name.__len__())