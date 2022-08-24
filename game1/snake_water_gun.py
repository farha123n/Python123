import random

def game(com1,you):
    if com1==user:
        return None
    elif com1=='s':
        if you=='g':
          return True
        if you=='w':
            return False
    elif com1=='w':
        if you=='s':
            return False
        if you=='g':
            return True
    elif com1=='g':
        if you=='s':
            return False
        if you=='w':
            return True
        





randinfo=random.randint(1,3)
if randinfo==1:
    com='s'
if randinfo==2:
    com='w'
if randinfo==3:
    com='g'

user=input("enter snake(s) water(w) gun(g)")
print(user)
a=game(com,user)
if a==None:
    print("it's a tie")
if a==True:
    print("you won")
if a==False:
    print("you won")