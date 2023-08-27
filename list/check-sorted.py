def checkSort(l):
    if len(l)<=1:
        return True
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            return False
    return True
l=[10,20,20,30]
print(checkSort(l))

#using sorted function

def isSort(l):
    sl=sorted(l)
    if sl==l:
        return True
    return False
l=[10,20,20,0]
print(isSort(l))