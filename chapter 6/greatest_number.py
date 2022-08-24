a=int(input("enter number1 "))
b=int(input("enter number2 "))
c=int(input("enter number3 "))
d=int(input("enter number4 "))
if(a>b):
    if(a>c):
        if(a>d):
            print("a is greates number")
        else:
            print("d is greater number")
    elif(c>d):
        print("c is greatest number")
    else:
        print("d is greater number")
elif(b>c):
    if(b>d):
        print("b is greatest number")
    else:
        print("d is grater number")
elif(c>d):
        print("c is greatest number")
else:
    print("d is greatest number")