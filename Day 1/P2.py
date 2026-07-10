
#Parent class 

class Animal:
    def __init__(self,name):
        self.name = name

    def makeSound(self):
        return "Some sound"
    
# Child class

class Cat(Animal):
    def makeSound(self):
        return f"{self.name} says meow" 
    
#Child class

class Cow(Animal):
    def makeSound(self):
        return f"{self.name} says moo"    
    
cat = Cat("Billu") 
cow = Cow("Jerry")

print(cat.makeSound())
print(cow.makeSound())