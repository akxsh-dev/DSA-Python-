def intersection(a,b):
    i=0
    j=0
    while i<len(a) and j< len(b):
        if a[i]==a[i-1]:
            i+=1
        elif b[j]==b[j-1]:
            j+=1

        elif a[i]<b[j]:
            i+=1
        elif b[j]<a[i]:
            j+=1

        else:
            print(a[i],end=" ")
            i+=1
            j+=1
a=[2,3,3,3,8,15,18,18,48]
b=[2,3,17,17,18,49]
c=intersection(a,b)

