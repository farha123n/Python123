s1=int(input("Enter number of  subject1"))
s2=int(input("Enter number of  subject2"))
s3=int(input("Enter number of  subject3"))

ave=(s1+s2+s3)/3
if(ave>40):
    if(s1>33 and s2>33 and s3>33):
        print("pass")
    else:
        print("fail")
else:
    print("fail")

