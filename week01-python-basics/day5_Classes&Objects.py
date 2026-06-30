
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.species)


class Demo(object):
    z = 30

    def __init__(self):
        self.x = 10 #instance variable
        self.y = 20

    def instFun(self):
        print("Instance method")

    @classmethod
    def clsFun(cls):
        print("Class method")

    @staticmethod
    def staticFun():
        print("Static method")

obj = Demo()