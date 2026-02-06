# create classes
class human:

    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
        print("I am a human")
        print("My name is", self.name)
        print("My age is", self.age)


class man(human):  # inheritance

    def __init__(self, name, age, gender):  # constructor
        super().__init__(name, age)  # call parent constructor
        self.gender = gender
        print("I am a man")
        print("My gender is", self.gender)


class woman(human):  # inheritance

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
        print("I am a woman")
        print("My gender is", self.gender)


class child(human):  # inheritance

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
        print("I am a child")
        print("My gender is", self.gender)


# create objects
human1 = human("John", 30)
man1 = man("John", 30, "male")
woman1 = woman("Jane", 25, "female")
child1 = child("Jack", 5, "male")
# print objects
print(human1)
print(man1)
print(woman1)
print(child1)
# print attributes
print(human1.name)
print(human1.age)
