def fact(n):
    if (n==0):
        return 1
    return n*fact(n-1)
n=5
factorial_of_n = fact(n)
print("Factorial of", n, "is", factorial_of_n)