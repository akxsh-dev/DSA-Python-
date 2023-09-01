def merge(list,low,high,mid):

    left=list[low:mid+1]
    right=list[mid+1:high+1]

    i=0
    j=0
    k=low

    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            k += 1
            i += 1
        else:
            list[k]=right[j]
            k+=1
            j+=1

    while i<len(left):
        list[k] = left[i]
        k += 1
        i += 1

    while j<len(right):
        list[k] = right[j]
        k += 1
        j += 1

def mergesort(list,l,r):
    if r>l:
        m=(r+l)//2
        mergesort(list,l,m)
        mergesort(list,m+1,r)
        merge(list,l,r,m)

    return list

list=[10,15,20,40,8,11,55]
result= mergesort(list,0,len(list)-1)
print(" THE SORTED LIST AFTER USING MERGE SORT: ", result)



