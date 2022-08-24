from string import whitespace


class Animal:
    AnimalType="mammal"
class pet(Animal):
    color='white'
class dog(pet):
    @staticmethod
    def  bark():
        print("bow bow")
d=dog()
d.bark()


