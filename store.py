def price(item):
    if item<10:
        total=item*120
        return total
    elif 10<=item<=99:
        total=item*100
        return total
    elif item>=100:
        total=item*70
        return total
item=int(input("enter no of items "))
cost=price(item)
print ("total price is ",cost)