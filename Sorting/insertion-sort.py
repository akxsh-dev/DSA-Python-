def insertionsort(list):
    n=len(list)
    for i in range(1,n):                #We start our iteration from the second element
        x=list[i]                       # x is the second element
        j=i-1                           # we are comparing it with previous element and storing it in j
        while j>=0 and list[j]>x:       #We are traversing backwards and the condintion is if index j is greater than or equal to 0 and its value is greater than x which is the second element or the element just forward to it
            list[j+1]=list[j]           #we update the J+1 index with J
            j-=1                        #decrement by 1
        list[j+1]=x                     #update that j+1 idx with x
    return list

list=[2,8,5,7,10]
new= insertionsort(list)
print(new)

# Best case: Theta of N
# Worst Case: Theta of N^2