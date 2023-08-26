#python has inbuilt function max() 'print(max(l)) to get the job done but lets write our own function


#Time complexity of this program is O(n^2)
def largest(l):
    for x in l:
        for y in l:
            if y>x:
                break
        else:
            return x

    return None #if we provide an empty list this will return none

l=[10,35,40,112,399]
print(largest(l))

#optimal approach
#time complexity O(n)
def largest(l):
    if not l:
        return None
    res=l[0]
    for i in range(1,len(l)):
        if l[i]>res:
            res=l[i]
    return res
l=[10,35,40,112,39]
print(largest(l))
