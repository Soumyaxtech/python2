x = int(input("enter 1st number "))
y = int(input("enter 2nd number "))
try:
    z = x/y              #********THIS IS CALLED EXCEPTION HANDLING WE HAVE TO WRITE
except Exception as e:    # (try:then the code where exception might occur then except ---------)
    print("exception is", e)
    z = None
print("the ans is", z)
