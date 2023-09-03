def partition(list,p):
    n=len(list)
    list[p],list[n-1]=list[n-1],list[p]
    temp=[]
    for i in list:
        if i<=list[n-1]:
            temp.append(i)
    for i in list:
        if i>list[n-1]:
            temp.append(i)
    for i in range(len(list)):
        list[i]=temp[i]

    return list
list=[5,3,6,9,12,8,11]
p=5
res=partition(list,p)
print(res)

