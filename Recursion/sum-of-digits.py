def sumofdigits(n):
    if n<10:
        return n
    return sumofdigits(n//10) + n%10        #% is used for the last digit and // is used to get the first digits

n=int(input("Enter a value: "))
res= sumofdigits(n)
print(res)