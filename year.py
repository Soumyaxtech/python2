def is_year(year):
    return(year%4==0 and year%100 !=0 or year%400==0)
    #     print(year,"is a leap year")
    # else:
    #     print(year,"is not a leap year")
year=int(input("enter the year "))
if is_year(year):
    print(year,"is leap year")
    days=1*366
    print(year,"has",days,"days")
    hours=366*24
    print(year, "has", hours, "hours")
else:
    days=1*365
    print(year,"has",days,"days")
    hours = 365 * 24
    print(year, "has", hours, "hours")