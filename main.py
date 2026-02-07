# First, we create a Class
class Human:

    def __init__(
        self, name, age, gender
    ):  # constructor is a special method that is called when an object is created
        # attributes
        self.name = name
        self.age = age
        self.gender = gender
        print("I am a human")
        print("My name is", self.name)
        print("My age is", self.age)
        print("My gender is", self.gender)

# now we create methods

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

    def work(self):
        print("I am working")


# Now we create an object of the class
me = Human("Rafee", 14, "Male")
print("---------------------------------")
brother = Human("Abdullah", 10, "Male")

print(brother.name)  # getter method
brother.name = "Mohammed Abdullah"  # setter method
print(brother.name)

me.eat()
brother.sleep()

# # create classes
# class human:

#     def __init__(self, name, age):  # constructor
#         self.name = name
#         self.age = age
#         print("I am a human")
#         print("My name is", self.name)
#         print("My age is", self.age)

#     # create methods
#     def eat(self):
#         print("I am eating")

#     def sleep(self):
#         print("I am sleeping")

#     def work(self):
#         print("I am working")

# human1 = human("Yawar", 41)
# human1.eat()
# human1.sleep()
# human1.work()

# class man(human):  # inheritance

#     def __init__(self, name, age, gender):  # constructor
#         super().__init__(name, age)  # call parent constructor
#         self.gender = gender
#         print("I am a man")
#         print("My gender is", self.gender)

# class woman(human):  # inheritance

#     def __init__(self, name, age, gender):
#         super().__init__(name, age)
#         self.gender = gender
#         print("I am a woman")
#         print("My gender is", self.gender)

# class child(human):  # inheritance

#     def __init__(self, name, age, gender):
#         super().__init__(name, age)
#         self.gender = gender
#         print("I am a child")
#         print("My gender is", self.gender)

# # create objects
# human1 = human("John", 30)
# man1 = man("John", 30, "male")
# woman1 = woman("Jane", 25, "female")
# child1 = child("Jack", 5, "male")
# # print objects
# print(human1)
# print(man1)
# print(woman1)
# print(child1)
# # print attributes
# print(human1.name)
# print(human1.age)
