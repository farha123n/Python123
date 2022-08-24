class c2d:
    def __init__(self,x,y) :
        self.x=x
        self.y=y

class c3d(c2d):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z=z
vector =c3d(1,5,9)
vector.x=12
print(vector.x)

            