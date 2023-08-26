def getSmall(l,n):
    res=[]
    for i in l:
        if i<n:
            res.append(i)
    return res
l=[1,2,3,4,5,6,7,8,9,10]
n=int(input("Enter a value: "))
result=getSmall(l,n)
print(result)

#using comprehension
def getSmall(l,n):
    return [i for i in l if i< n]
l=[1,2,3,4,5,6,7,8,9,10]
n=int(input("Enter a value: "))
result=getSmall(l,n)
print(result)