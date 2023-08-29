# TODO: you are given a sorted list which contain only binary elements count the number of 1's
#Brute Force Method
def countOne(list):
    n=len(list)
    count=0
    for i in range(0,n):
        if list[i]==1:
            count+=1
    return count

list=[0,1,1,0,1,1,0,1,0,1]
res=countOne(list)
print("1 is present",res,"no of times")
