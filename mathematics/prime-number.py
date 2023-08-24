def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


Value = int(input("Enter a number to check prime or not:"))
result = isPrime(Value)
print(result)


#better Solution
# we are using x^2<=n concept here, lets say if a number n has (x,y) divisor and lets say x<y
#its safe to assume that the square root of the number would also be greater than the smallest divisor
#by this method we dont need to check individual digits till n to check if its divisible or not
# def isPrime(n):
#     if n == 1:
#         return False
#     i = 2
#     while (i * i <= n):         #i is the squared divisor that is being compared to the number
#
#         if n % i== 0:
#             return False
#         i += 1
#     return True
# Value = int(input("Enter a number to check prime or not:"))
# result = isPrime(Value)
# print(result)


#Optimal solution
# First we are checking if its even or odd, if it is then it would save us a lot of time and return false
#
# def isPrime(n):
#     if n==1:
#         return False
#     if n==2 or n==3:
#         return True
#     if n%2==0 or n%3==0:        #checking even or odd
#         return False
#
#     i=5
#     while (i*i<=n):
#         if n%i==0 or n%(i+2)==0:       #checking if the number is divisible by 5 or 7 at once
#             return False
#         i +=6                           #incrementing by 6
#     return True
#
# Value = int(input("Enter a number to check prime or not:"))
# result = isPrime(Value)
# print(result)









