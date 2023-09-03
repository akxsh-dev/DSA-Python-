#refer notes to understand this logic
def partition(list,l,h):
    pivot=list[h]
    i=l-1
    for j in range(l,h):
        if list[j]<pivot:
            i+=1
            list[i],list[j]=list[j],list[i]

    list[i+1],list[h]=list[h],list[i+1]
    return i+1

list=[10,80,30,90,50,70]
res=partition(list,0,len(list)-1)
print(res)