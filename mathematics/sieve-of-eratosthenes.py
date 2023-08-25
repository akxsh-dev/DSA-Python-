#Sieve of Eratosthenes is a method for finding all primes up to (and possibly including) a given natural.
# This method works well when is relatively small, allowing us to determine whether any natural
# number less than or equal to is prime or composite.

def isPrime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+5)==0:
            return False
        i+=6
    return True
def printPrime(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(i, end=" ")

n= int(input("enter a value:"))
printPrime(n)
