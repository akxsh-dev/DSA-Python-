def rootfloor(n):
    i=1
    while i*i <= n:
        i+=1
    return i-1
n=int(input("Enter a number you want to calculate the floor Square root of: "))
print(rootfloor(n))


#using Binary Search

def floorRoot(n):
    low=1
    high=n
    res=-1

    while low<=high:
        mid=(low+high)//2
        mid_sq= mid*mid
        if mid_sq==n:
            return mid
        elif n<mid_sq:
            high=mid-1
        else:
            low=mid+1
            res=mid
    return res

n=int(input("Enter a number you want to calculate the floor Square root of: "))
print(floorRoot(n))
