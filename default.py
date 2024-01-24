def sum(a,b=0):
    """
    IF WE DON'T PASS VALUE OF b THEN IT WILL ASSUME IT 0 THIS IS CALLED DEFAULT
    BUT IF B VALUE GIVEN THEN IT WILL TAKE THE VALUE  (it is called documentation string )
    """
    print("a=",a)
    print("b=",b)
    total=a+b
    print("total is ",total)
    return total
n=sum(4,10)