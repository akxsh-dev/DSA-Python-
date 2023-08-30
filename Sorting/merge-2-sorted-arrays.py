# to understand merge sort lets first understand how 2 sorted arrays gets merged

#this is naive solution
#time complexity: (m+n)*log(m+n)
#this doesnt consider the fact that our input lists are sorted or not
#TODO:
# def merge(a,b):
# res=a+b
# res.sort()
# print(res)

#efficient solution

def merge(a,b):
    m=len(a)
    n=len(b)
    res=[]                          #initializing an empty list to append values
    i=0
    j=0
    while i<m and j<n:              #iterators shouldnt be greater than length of aither of the lists
        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1

    while i<m:                      #if one of the iterators exceed its own length, just append remaining elements from the other list
        res.append(a[i])
        i+=1
    while j<n:
        res.append(b[j])
        j+=1

    return res

a=[10,15]
b=[5,6,6,30,40]
c=merge(a,b)
print(c)