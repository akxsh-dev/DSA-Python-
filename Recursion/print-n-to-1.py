def printto1(n):
    if n<1:
        return n
    print(n, end=" ")
    printto1(n-1)

n=3
printto1(n)