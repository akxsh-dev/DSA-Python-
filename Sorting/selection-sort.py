# find the minimum element first and put it first index and so on
def selectionsort(list):
    n=len(list)
    for i in range(n-1):

        min_idx=i                           # This
        for j in range(i+1,n):              # Block of code
            if list[j]<list[min_idx]:       # Finds
                min_idx=j                   # Minimum Element Beginning from I

        list[min_idx],list[i]= list[i],list[min_idx]
    return list

list=[2,8,5,7,10]
new= selectionsort(list)
print(new)

