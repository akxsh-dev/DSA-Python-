# we will use Euclidean Algorithm in this

#Naive Logic
# def hcf(a,b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     return a
#
# n1= int(input("enter first value:"))
# n2=int(input("enter second value:"))
# result= hcf(n1,n2)
# print(result)


#optimised code
def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
n1= int(input("enter first value:"))
n2=int(input("enter second value:"))
result= hcf(n1,n2)
print(result)


