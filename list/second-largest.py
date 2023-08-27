def getsecmax(l):
    if len(l)<=1:           #we are checking if the list is empty or is it containing a single value
        return None         #either the case will return none

    lar= largest(l)         #getting the largest number from the other function
    slar= None
    for x in l:
        if x!=lar:
            if slar==None:
                slar=x
            else:
                slar=max(slar,x)
    return slar
def largest(l):
    res=l[0]
    for i in range(1,len(l)):
        res= max(res,l[i])
    return res
l=[10,35,40,112,39]
print(getsecmax(l))


#optimal solution with a single traversal

def getsecmax(l):
    if len(l)<=1:
        return None

    lar=l[0]
    slar=None

    for i in l[1::]:
        if i>lar:
            slar=lar
            lar=i
        elif i!=lar:
            if slar==None or slar<i:
                slar=i
    return slar
l=[10,35,40,112,51]
print(getsecmax(l))

