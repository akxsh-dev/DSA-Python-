#Returns the index of the element you want to search in a SORTED array/list and returns -1 if item is not present
# logic: we are diving the list into 3 parts. the mid, values before mid, and the values after mid
#first condition is that if the item we are going to search is mid then we are returning mid directly
#Second condition: if the value is greater than mid(since its sorted) we are updating the low value to mid+1
#third condion is if the value is lesser than the mid(since its sorted) we are updating the high value to mid-1
def BinarySearch(list,x):
    low=0
    high= len(list)-1
    while low<=high:
        mid=(low+high)//2

        if list[mid]==x:
            return mid

        elif list[mid]<x:
            low= mid+1

        else:
            high=mid-1

    return -1

list=[10,20,30,40,50]
n= int(input("Enter the value from the Sorted List that you want to search: "))
result=BinarySearch(list,n)
print("THE INDEX OF THE VALUE IS", result)


#Recursive approach
def bsearch(l,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2

    if l[mid]==x:
        return mid

    elif l[mid]<x:
        return bsearch(l,x,mid+1,high)
    else:
        return bsearch(l,x,low,mid+1)

def bsearchmain(list,n):                            #This is a wrapper function that allows user to use minimum parameters
    return bsearch(list,n,0, len(list)-1)

list=[10,20,30,40,50,60,70]
n= int(input("Enter the value from the Sorted List that you want to search: "))
result=bsearchmain(list,n)
print("THE INDEX OF THE VALUE IS", result)

