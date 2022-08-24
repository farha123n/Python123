class complex:
    def __init__(self,r,c) :
        self.r=r
        self.c=c
    def __add__(self,c):
        return complex(self.r+c.r,self.c+c.c)
    def __str__(self):
        return f"{self.r}+{self.c}i"

c1=complex(12,7)
c2=complex(13,15)
print(c1+c2)