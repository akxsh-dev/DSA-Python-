#TODO:
# Input: [3,5,8] [2,8,9,10,15]
# output: [2,3,5,8,9,10,15]
#

#naive solution
# def union(l1,l2):
#     l3=l1+l2
#     l3.sort()
#     for i in range (0,len(l3)):
#         if(i==0 or l3[i]!=l3[i-1]):
#             print(l3[i],end=" ")
#
# l1=[3,5,8]
# l2=[2,8,9,10,15]
# res=union(l1,l2)
# print(res)


#Using merge sort
def union(a,b):
    i=0
    j=0
    while i<len(a) and j<len(b):            #we will come out of this while loop once i and j become equal to length of either of list

        if a[i]==a[i-1]:                    #if we encounter duplicates we are increamenting and just ignoring them
            i+=1
        elif b[j]==b[j-1]:
            j+=1

        elif a[i]<b[j]:                     #the smallest of either of the list gets printed first
            print(a[i],end=" ")
            i+=1
        elif b[j]<a[i]:
            print(b[j],end=" ")
            j+=1

        else:                               #if we encounter the same element in either of the list print any and increment both lists iterators by 1
            print(a[i],end=" ")
            i+=1
            j+=1

    while i<len(a):
        if i>0 and a[i]!=a[i-1]:
            print(a[i],end=" ")
        i+=1

    while j<len(b):
        if j>0 and b[j]!=b[j-1]:
            print(b[j], end=" ")
        j+=1

a=[10,15]
b=[2,3,17,18,49]
c=union(a,b)
