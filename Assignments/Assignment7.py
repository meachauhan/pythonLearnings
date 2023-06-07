n=int(input("Enter any number:"))
primeFlag=True
if n==1: print("Prime number")
else:
    for i in range(2,n-1):
        if n%i==0:
            primeFlag=False
    if primeFlag: print("Prime number")
    else: print("Not a prime number")