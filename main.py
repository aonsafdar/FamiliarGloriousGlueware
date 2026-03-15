# # # # First, we create a Class
# # # class Human:

# # #     def __init__(self, name, age, gender):   #constructor is a special method that is called when an object is created
# # #         # attributes
# # #         self.name = name
# # #         self.age = age
# # #         self.gender = gender
# # #         print("I am a human")
# # #         print("My name is", self.name)
# # #         print("My age is", self.age)
# # #         print("My gender is", self.gender)

# # # # now we create methods

# # #     def eat(self):
# # #         print("I am eating")

# # #     def sleep(self):
# # #         print("I am sleeping")

# # #     def work(self):
# # #         print("I am working")

# # # # Now we create an object of the class
# # # me = Human("Rafee", 14, "Male")
# # # print("---------------------------------")
# # # brother = Human("Abdullah", 10, "Male")

# # # print(brother.name) # getter method
# # # brother.name = "Mohammed Abdullah" # setter metho
# # # print(brother.name)

# # # me.eat()
# # # brother.sleep()

# # # print(f"My name is {me.name} and I am {me.age} years old and I am a {me.gender}")
# # # # # create classes
# # # # class human:

# # # #     def __init__(self, name, age):  # constructor
# # # #         self.name = name
# # # #         self.age = age
# # # #         print("I am a human")
# # # #         print("My name is", self.name)
# # # #         print("My age is", self.age)

# # # #     # create methods
# # # #     def eat(self):
# # # #         print("I am eating")

# # # #     def sleep(self):
# # # #         print("I am sleeping")

# # # #     def work(self):
# # # #         print("I am working")

# # # # human1 = human("Yawar", 41)
# # # # human1.eat()
# # # # human1.sleep()
# # # # human1.work()

# # # # class man(human):  # inheritance

# # # #     def __init__(self, name, age, gender):  # constructor
# # # #         super().__init__(name, age)  # call parent constructor
# # # #         self.gender = gender
# # # #         print("I am a man")
# # # #         print("My gender is", self.gender)

# # # # class woman(human):  # inheritance

# # # #     def __init__(self, name, age, gender):
# # # #         super().__init__(name, age)
# # # #         self.gender = gender
# # # #         print("I am a woman")
# # # #         print("My gender is", self.gender)

# # # # class child(human):  # inheritance

# # # #     def __init__(self, name, age, gender):
# # # #         super().__init__(name, age)
# # # #         self.gender = gender
# # # #         print("I am a child")
# # # #         print("My gender is", self.gender)

# # # # # create objects
# # # # human1 = human("John", 30)
# # # # man1 = man("John", 30, "male")
# # # # woman1 = woman("Jane", 25, "female")
# # # # child1 = child("Jack", 5, "male")
# # # # # print objects
# # # # print(human1)
# # # # print(man1)
# # # # print(woman1)
# # # # print(child1)
# # # # # print attributes
# # # # print(human1.name)
# # # # print(human1.age)

# import requests

# class Joke:

#   def __init__(self):
#     self.setup = ''
#     self.punchline = ''

#   def fetch(self):
#     url = 'https://official-joke-api.appspot.com/random_joke'
#     r = requests.get(url, timeout=10)
#     r.raise_for_status()
#     data = r.json()
#     self.setup = data['setup']
#     self.punchline = data['punchline']

#   def show(self):
#     print(self.setup)
#     print(self.punchline)

# # the class finishes her

# j = Joke()  # create object

# # let fetch and display 5 jokes through a for loop
# for i in range(5):
#   try:  # if the internet is dead
#     j.fetch()  # calling the fetch function on the j object
#     print(f"Joke {i+1}")
#     j.show()  #calling the show function on the j object
#   except requests.exceptions.RequestException:
#     print('Could not fetch a joke. Check internet and try again.')

# # Creating sample class
# # class Test:

# #   def __init__(self, a, b):
# #     self.a = a
# #     self.b = b
# #     print("Test class constructor executed....")
# # # create a method to add two numbers
# # # Try to do exception handling using try and except block

# #   def divide(self):
# #     try:
# #       print("before exception")
# #       print("Division of two numbers: ", self.a / self.b)
# #       print("after exception")
# #     except ZeroDivisionError:
# #       print("You can't divide a number by zero")

# # # Object creation
# # obj = Test(1, 3)
# # obj.divide()

import random


# this is the class code
class Character:  # class

  def __init__(self, name, hp):
    self.name = name
    self.hp = hp

  def show_status(self):
    print(f"{self.name} has {self.hp} health points remaining.")

  def is_alive(self):
    if self.hp > 0:
      #print(f"{self.name} is alive")
      return True
    else:
      #print(f"{self.name} is dead")
      return False

  def attack(self, other_player):
    damage = random.randint(1, 20)
    other_player.hp -= damage
    if other_player.hp < 0:
      other_player.hp = 0
    print(f"{self.name} attacks {other_player.name} for {damage} damage.")

  def heal(self):
    heal_amount = random.randint(1, 20)
    self.hp += heal_amount
    print(f"{self.name} heals for {heal_amount} health points.")


# # create an object
# hero = Character("Batman", 100)
# hero.show_status()
# hero.is_alive()

# enemy = Character("Joker", 100)
# enemy.show_status()
# enemy.is_alive()

# hero.attack(enemy)
# enemy.show_status()
# enemy.is_alive()
# enemy.heal()
# enemy.show_status()

def main():
  print("=== MINI RPG BATTLE ===")
  player_name = input("Enter your name: ")
  if player_name == "":
    player_name = "Hero"
  player = Character(player_name, 100)
  
  
  enemy = Character("Goblin", 100)
  print(f"\n A wild {enemy.name} appears!")


  round_num = 1
  while player.is_alive() and enemy.is_alive(): # while both are alive the game should continue
    print(f"\n--- Round {round_num} ---")
    player.show_status()
    enemy.show_status()

    print("\nChoose an action:")
    print("1. Attack")
    print("2. Heal")
    choice = input("Enter your choice (1 or 2): ")

    # PLayer's turn
    if choice == "1":
      player.attack(enemy)
    elif choice == "2":
      player.heal()
    else:
      print("Invalid choice. Please try again.")

    # check if enemy died after player's turn
    if not enemy.is_alive():
      print(f"\n{enemy.name} has been defeated! You win!")
      break

    # Enemy's turn
    print(f"\n{enemy.name}'s turn.")
    enemy.attack(player)
    round_num +=1
    print('\n=== BATTLE RESULT ===')

    player.show_status()
    enemy.show_status()

  if player.is_alive():
    print(f"You win, {player.name}!")
  else:
    print('You lost! Try again.')
    
      
  


main()