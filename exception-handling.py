x = (input("enter 1st number "))
y = (input("enter 2nd number "))
try:
    z = int(x)/int(y)             #********THIS IS CALLED EXCEPTION HANDLING WE HAVE TO WRITE
except ZeroDivisionError as e:    # (try:then the code where exception might occur then except ---------)
    print("exception is", e)
    z = None
print("the ans is", z)
# except TypeError as e:
#     print("typeerror occur")  #except Exception as e
                               # print("error is ",type(e))
#     z=None
# print("the ans is", z)
