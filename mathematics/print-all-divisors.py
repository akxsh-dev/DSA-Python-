# brute force
# def printDivisors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
#
#
# n=int(input("enter a value:"))
# printDivisors(n)


#Efficient solution
#NOTE: we are using x^2<=n concept here, lets say if a number n has (x,y) divisor and lets say x<y
#its safe to assume that the square root of the number would also be greater than the smallest divisor
#this doesnot return in ascending
# def printDivisors(n):
#     i=1
#     while (i*i<=n):
#       if(n%i==0):
#           print(i)
#           if(i!=n//i):
#               print(n//i)
#       i+=1
#
# x= int(input("Enter the value: "))
# printDivisors(x)

#optimal solution
#return the divisor in sorted order
def printDivisors(n):
    i=1
    while(i*i<n):
        if(n%i==0):
            print(i)
        i+=1

    while(i>=1):
        if(n%i==0):
            print(n//i)
        i-=1

n = int(input("enter a value:"))
printDivisors(n)


