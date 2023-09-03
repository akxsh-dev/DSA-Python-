def hoarespartition(list,l,h):
    pivot=list[l]
    i=l-1
    j=h+1

    while True:
        i+=1
        if list[i]<pivot:
            i+=1

        j-=1
        if list[j]>pivot:
            j=j-1

        if i>=j:
            return j
        list[i],list[j]=list[j],list[i]

list=[5,3,8,4,2,7,1,10]
res=hoarespartition(list,0,len(list)-1)
print(res)