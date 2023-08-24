# if number = 89172 output should be 5
#logic: divide by 10
# use // to not get a floating value while traversing

n= int(input("enter a number:"))
result= 0
while n>0:
    n= n//10
    result = result +1
print("count of the digits is:" + " " + str(result))

# n = int(input("enter a number:"))
# result = 0
# for _ in str(n):
#     result += 1
# print("count of the digits is:", result)