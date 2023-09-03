#we are using Lomuto partition here
# def lPartition(list,l,h):
#     pivot=list[h]
#     i=l-1
#     for j in range(l,h):
#         if list[j]<pivot:
#             i+=1
#             list[i],list[j]=list[j],list[i]
#
#     list[i+1],list[h]=list[h],list[i+1]
#     return i+1
#
# def quicksort(list,l,h):
#     if l<h:
#         p=lPartition(list,l,h)
#         quicksort(list,l,p-1)
#         quicksort(list,p+1,h)
#     return list
# list=[10,80,30,90,50,70]
# res=quicksort(list,0,len(list)-1)
# print(res)


def hPartition(list,l,h):
    pivot=list[l]
    i,j=l-1,h+1

    while True:
        i+=1
        if list[i]<pivot:
            i+=1
        j-=1
        if list[j]>pivot:
            j-=1
        if i>=j:
            return j
        list[i],list[j]=list[j],list[i]

def qsort(list,l,h):
    if l<h:
        p=hPartition(list,l,h)
        qsort(list,l,p)
        qsort(list,p+1,h)
    return list
list=[8,4,7,9,3,10,5]
res=qsort(list,0,len(list)-1)
print(res)