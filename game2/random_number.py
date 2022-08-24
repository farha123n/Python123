import random

r=random.randint(1,100)
guess_num=0
flage=True

number=int(input("Enter a number between 1 to 100: "))
while(flage):
    guess_num=guess_num+1
    if number>r:
      number =  int(input("Enter a small number: "))
      
    elif number<r:
     number = int(input("enter a big number: "))
     
    elif number==r:
        
        print("you won")
        print(f"number of gusses {guess_num}")
        flage=False    
    
with open("highScore.txt",'r') as f:
     highscore=int(f.read())
if guess_num<highscore:
   print("congrates!, you have break the high score") 
   with open("highScore.txt",'w') as f:
    f.write(str(guess_num))