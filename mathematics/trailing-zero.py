# write a program to calculate trailing zeroes in a factorial of a number
#for example 5! = 120, output: 1




#Brute Force Method
#Time complexity is O(n)
# def countZeroes(n):
#     fact = 1
#     for i in range(2, n+1):
#         fact= fact*i
#
#     count = 0
#     while(fact%10 == 0):
#         count= count + 1
#         fact = fact // 10
#
#     return count
#
# n= int(input("Enter a Value:"))
# result = countZeroes(n)
# print(result)

# #optimal solution better code
# # product of 5&2 is 10, so if we can count the number of 5's, 25(5*5),125 and so on in factorial of a given number
def countZeroes(n):
    count= 0
    i=5
    while i<=n:
        count=count + n//i
        i=i*5

    return count

n= int(input("Enter a Value:"))
result = countZeroes(n)
print(result)








