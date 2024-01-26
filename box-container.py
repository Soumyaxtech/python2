def count_box(cookies):
    box=(cookies//24)
    leftcookies=(cookies%24)
    return box,leftcookies
def count_container(cookies):
    container = ((cookies // 24) // 75)
    leftboxes = ((cookies // 24)% 75)
    return container, leftboxes
cookies=int(input("enter number of cookies "))
k1=count_box(cookies)
k2=count_container(cookies)
print("boxes and leftoverCookies respectively",k1)
print("containers and leftoverBoxes respectively",k2)