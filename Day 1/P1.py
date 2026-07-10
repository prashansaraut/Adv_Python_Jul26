
class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof! and it is {self.age} years old"

# Create object
my_dog = Dog("Jerry",3)
my_dog2 = Dog("Tom",4)

print(my_dog.bark())
print(my_dog2.bark())