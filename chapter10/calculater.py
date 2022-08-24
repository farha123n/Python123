class Calculator:
    def __init__(self,number) :
        self.n=number
    def square(self):
        print(f"the square of number {self.n} is {self.n**2}")
    def squareRoot(self):
        print(f"the square root of number {self.n} is {self.n**.5}")
    def cube(self):
       print(f"the cube of number {self.n} is {self.n**3}")
cal=Calculator(3)
cal.square()
cal.cube()
cal.squareRoot()
    
