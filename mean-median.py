def mean(numbers):
    total=sum(numbers)
    return total/len(numbers)
def median(numbers):
    sortednum=sorted(numbers)
    if len(sortednum)%2==0:
        median1=(sortednum[len(sortednum)//2-1]+sortednum[len(sortednum)//2])/2
    else:
        median1=sortednum[len(sortednum)//2]
    return median1
numbers=[4,5,6,8,9]
mean=mean(numbers)
print(mean)
median=median(numbers)
print(median)