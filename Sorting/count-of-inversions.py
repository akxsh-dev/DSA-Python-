# Naive solution
# def countinversions(list):
#     count=0
#     for i in range(len(list)-1):
#         for j in range(i+1,len(list)):
#             if list[i]>list[j]:
#                 count+=1
#     return count
# list=[40,30,20,10]
# result= countinversions(list)
# print(result)


#efficient solution
def countinverse(list,l,r):
    res=0
    if l<r:
        m=(l+r)//2
        res+=countinverse(list,l,m)
        res+=countinverse(list,m+1,r)
        res+=merge(list,l,m,r)
    return res
def merge(list,l,m,r):
    left=list[l:m+1]
    right=list[m+1:r+1]

    res,i,j,k=0,0,0,l

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            list[k]=left[i]
            i+=1
        else:
            list[k]=right[j]
            j+=1
            res+=(len(left))-i
        k+=1

    while i<len(left):
        list[k] = left[i]
        i += 1
        k += 1

    while j<len(right):
        j += 1
        res += len(left) - i
        k += 1
    return res
list=[40,30,20,10]
result= countinverse(list,0,len(list)-1)
print(result)


