# calculating total expances through-out the year*************************(1)


# exp = [250,980,673,123,789,556,800,230,456,890,900,1600]
# total = 0
# for i in range(len(exp)):
#     print("month ",i+1, ": expances ",exp[i])
#     total=total+exp[i]
# print ("total expances through-out year ",total)

# printing 1-10 using for loop***************************(2)

# for i in range(0,10):
#     print (i+1)   # i is a variable here


# find car key from given locations**************************(3)

# key_location="table"
# loc=["bed","chair","garage","dinning","table","sofa"]
# for i in loc:
#     if i==key_location:
#         print("key is found in",i)
#         break      # when key is found it's not going to search again so break statement
#     else:
#         print("key is not found in",i)

# print squre of odd numbers **********************************(4)

sum=0
for i in range(1,11):
    if i%2==0:
        continue
    print(i*i)
    sum=sum +(i*i)
print("the total is ",sum)
