#Brute Force Method
#we are going to traverse the length of the list in reverse

# def lastOcurrence(l,n):
#     for i in reversed(range(0,len(l))):             #Traversing in Reverse
#         if l[i]==n:
#             return i
#     return -1
#
# list=[1,1,1,1,5]
# x=int(input("Enter a value from the the list to return its index "))
# res= lastOcurrence(list,x)
# print(res)
#
# #Recursive Approach
#
# def lastOcurrence(list,x,low,high):
#     if low>high:
#         return -1
#     mid=(low+high)//2
#     if x>list[mid]:
#         return lastOcurrence(list,x,mid+1,high)
#     elif x<list[mid]:
#         return lastOcurrence(list,x,low,mid+1)
#     else:
#         if mid==0 or list[mid+1]!=list[mid]:
#             return mid
#         else:
#             return lastOcurrence(list,x,mid+1,high)
#
# def lastOcurrenceMain(list,x):
#     return lastOcurrence(list,x,0,len(list)-1)
#
# list=[10,20,20,30,30,30,40,40,50,60,70]
# x=int(input("Enter a value from the the list to return its index "))
# res= lastOcurrenceMain(list,x)
# print(res)

#Iterative approach

def lastOcurrence(list,x):
    low=0
    high=len(list)-1

    while low<=high:            #while low <= high instead of while low < high to ensure that the loop considers the last element of the list when necessary.
        mid=(low+high)//2
        if x>list[mid]:
            low=mid+1
        elif x<list[mid]:
            high=mid-1
        else:
            if mid == len(list) - 1 or list[mid+1]!=list[mid]:      # mid == len(list) - 1 is used to handle the case when the last element is the target value.
                return mid
            else:
                low=mid+1
    return -1
list=[1,1,1,1,5]
x=int(input("Enter a value from the the list to return its index "))
res= lastOcurrence(list,x)
print(res)

