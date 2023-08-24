#NOTE: if both values are co-prime the LCM would be the product of two values
#NOTE: if one the value is divisible by the other the LCM would be the higher value


#Brute Force Technique
# def lcm(a,b):
#     res= max(a,b)
#     while True:
#         if res%a==0 and res%b==0:
#             return res
#         res += 1
#     return res
#
# n1=int(input("Enter the first value:"))
# n2=int(input("enetr the second value:"))
# result= lcm(n1,n2)
# print(result)

#optimal approach
#note: lcm(a,b)= (a*b)/hcf(a,b)

def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)

def lcm(a,b):
    return (a*b)// hcf(a, b)

n1=int(input("Enter the first value:"))
n2=int(input("enetr the second value:"))
result= lcm(n1,n2)
print(result)




