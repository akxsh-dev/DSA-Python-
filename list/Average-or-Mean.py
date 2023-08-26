def mean(list):
    sum=0
    for i in list:
        sum=sum+i
    n=len(list)
    return sum/n
list= [10,20,30,40,50]
print(mean(list))

#using libraries

def average(l):
    return sum(l)//len(l)
l= [10,20,30,40,50]
print(average(l))