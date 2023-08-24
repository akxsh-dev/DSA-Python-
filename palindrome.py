#single digit number will always be palindrome number

n = int(input("Enter a number:"))

rev = 0
temp = n

while temp != 0:
    ld = temp % 10
    rev = rev * 10 + ld   #this variable rev is storing the value in the reverse
    temp = temp // 10

if n == rev:
    print("its a palindrome")
else:
    print("Its not a palindrome")

















  


