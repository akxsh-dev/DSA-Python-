# it will check the elements with the adjacent element and if its greater than the first element it will sort it +1 index and so on
#Time complexity : theta n^2
def bubblesort(list):
    n=len(list)
    for i in range(n-1):                #range(n-1) will give you values from 0 to n-2
        for j in range(n-i-1):          #n-1 will also work fine but its doing extra iteration and we are better coders
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list=[2,8,5,7,10]
new= bubblesort(list)
print(new)


#optimised code
# we are initializing a swapped variable as false, everytime it swaps it chanes to true

def bubbleSort(l):
    n=len(l)
    swapped = False
    for i in range(n-1):
        for j in range (n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped= True

    if swapped==True:
        return l
    else:
        print("list is already sorted")
        return swapped


list=[2,5,7,8,10]
new= bubbleSort(list)
print(new)


# worst case: BIG O of N
# best case : Linear time
# It is Stable in nature
