def mergesubarrays(a,low,mid,high):
    left=a[low:mid+1]               #mid+1 because slicing wont include the last element mid
    right=a[mid+1:high]
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if a[i]<=a[j]:
            a[k]=left[i]
            k = k + 1
            i = i + 1
        else:
            a[j]=right[j]
            k = k + 1
            j = j + 1
    while i<len(left):
        a[k]=left[i]
        k = k + 1
        i = i + 1
    while j<len(right):
        a[k]=right[j]
        k = k + 1
        j = j + 1

    return a

list=[10,15,20,40,8,11,55]
res= mergesubarrays(list,0,(0+len(list)-1)//2,len(list)-1)
print(res)