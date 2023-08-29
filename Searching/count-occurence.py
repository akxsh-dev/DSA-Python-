#Brute Force Method

def countOcurrence(list,x):
    count=0
    n=len(list)
    for i in range(0,n):
        if list[i]==x:
            count+=1
    return count

list=[1,1,1,1,5]
x=int(input("Enter a value from the the list to return its index "))
res= countOcurrence(list,x)
print(res)

#Efficient Solution
def firstoccur(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if x>l[mid]:
            low=mid+1
        elif x<l[mid]:
            high=mid-1
        else:
            if mid==0 or l[mid-1]!=l[mid]:
                return mid
            else:
                high=mid-1
    return -1

def lastoccur(l,x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if x > l[mid]:
            low = mid + 1
        elif x < l[mid]:
            high = mid - 1
        else:
            if mid == len(l)-1 or l[mid + 1] != l[mid]:
                return mid
            else:
                low=mid+1
    return -1

def countOcurrence(l,x):
    first= firstoccur(l,x)
    if first==-1:
        return 0
    else:
        return (lastoccur(l,x)-firstoccur(l,x))+1

list=[1,1,1,1,5]
x=int(input("Enter a value from the the list to return its index "))
res= countOcurrence(list,x)
print(res)