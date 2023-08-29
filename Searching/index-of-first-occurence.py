#Naive approach

def firstOcurrence(list,x):
    n= len(list)-1
    for i in range(0,n):
        if list[i]==x:
            return i
    return -1

list=[1,1,1,1,5]
x=int(input("Enter a value from the the list to return its index "))
res= firstOcurrence(list,x)
print(res)

#Efficient solution: We will use recursive binary search

def firstOcurrence(list,x,low,high):
    if low>high:
        return -1

    mid=(low+high)//2

    if x>list[mid]:
        return firstOcurrence(list,x,mid+1,high)
    elif x<list[mid]:
        return firstOcurrence(list,x,low,mid-1)
    else:
        if mid==0 or list[mid-1]!= list[mid]:           #this gives the first occurrence
            return mid
        else:
            return firstOcurrence(list,x,low,mid-1)

def firstOcurrenceMain(list,x):
    return firstOcurrence(list,x,0,len(list)-1)

list=[10,20,20,30,30,30,40,40,50,60,70]
x=int(input("Enter a value from the the list to return its index "))
res= firstOcurrenceMain(list,x)
print(res)


# Optimal Solution: We gonn use Iterative Binary Search

def firstOcurrence(list,n):
    low =0
    high= len(list)-1

    while low<high:
        mid = (low + high) // 2
        if n>list[mid]:
            low=mid+1
        elif n<list[mid]:
            high=mid-1
        else:
            if mid==0 or list[mid-1]!=list[mid]:
                return mid
            else:
                high=mid-1
    return -1

list=[10,20,20,30,30,30,40,40,50,60,70]
x=int(input("Enter a value from the the list to return its index "))
res= firstOcurrence(list,x)
print(res)
