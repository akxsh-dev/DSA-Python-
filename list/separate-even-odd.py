def separate(l):
    Even=[]
    Odd=[]
    for i in l:
        if i%2==0:
            Even.append(i)
        else:
            Odd.append(i)
    return Even, Odd
l=[1,2,3,4,5,6,7,8,9,10]
result= separate(l)
print(result)

#using comprehension
def separate(l):
    Even=[i for i in l if i%2==0]
    Odd=[i for i in l if i%2!=0]
    return Even, Odd
l=[1,2,3,4,5,6,7,8,9,10]
result= separate(l)
print(result)

