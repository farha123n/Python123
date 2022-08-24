def power(n,i):
    p=1
    if i>3:
        return pow(n,i-1)*n
    else:
        return 1
p=power(2,4)
print(p)