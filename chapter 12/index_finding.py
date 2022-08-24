list1=[5,8,7,6,5,90,87,65]
for index,item in enumerate(list1):
    if (index==3 or index==5 or index==7):
        print(f"{item}, {index}")