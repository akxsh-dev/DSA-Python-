# Simple Irterative code
# n = int(input("Enter a value:"))
# res = 1
# for i in range(2, n+1):
#     res=res*i
# print(res)
#
#

# recursive approach
def fact(n):
    if n == 0:
        return 1

    return n* fact(n-1)

n = int(input("Enter a value:"))
result = fact(n)
print(result)