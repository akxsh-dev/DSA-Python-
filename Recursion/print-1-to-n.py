def print2n(n):
    if n<1:
        return n
    print2n(n-1)
    print(n)

n=3
print2n(n)
