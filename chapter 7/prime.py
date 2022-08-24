n=int(input("enter number to check if it is prime "))
f=True
for i in range(2,n-1):
    if n%i==0:
        f=False
        break

if f:
    print("number is prime")
else:
    print("number is not prime")
    