# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
# a class called IceCreamStand that inherits from the Restaurant class you wrote 
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of 
# the class will work; just pick the one you like better. Add an attribute called 
# flavors that stores a list of ice cream flavors. Write a method that displays 
# these flavors. Create an instance of IceCreamStand, and call this method.
class Restaurant:
    def __init__(self, name, location, recipe):
        self.name = name
        self.location = location
        self.recipe = recipe

class IceCreamStand(Restaurant):
    def __init__(self, name, location, recipe):
        super().__init__(name, location, recipe)
        self.flavors = ["vanila flavor", "apple flavor", "orange flavor"]
    
    def display_flavor(self):
        print("The flavor types available at Restaurant is " + str(self.flavors))

branch = IceCreamStand("SpintexIce", "Spintex Accra", "butter") 
branch.display_flavor()

# 9-7. Admin: An administrator is a special kind of user. Write a class called 
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list 
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of 
# privileges. Create an instance of Admin, and call your method

# Solution
# from exercise import User

# class Admin(User):
#     def __init__(self, first_name,last_name,status,email):
#         super().__init__(first_name,last_name,status,email)
#         self.privileges = ["add post", "delete post", "ban user"]

#     def show_privileges(self):
#         show = "The administrator is eligible to " + str(self.privileges)
#         return show

# admin = Admin("Emmanuel","Adofo","Single","emmanueladofo011@gmail.com")
# print('\n')
# print(admin.show_privileges())

# 9-8. Privileges: Write a separate Privileges class. The class should have one 
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance 
# as an attribute in the Admin class. Create a new instance of Admin and use your 
# method to show its privileges.

from exercise import User

class Privileges:
    def __init__(self, privileges = "signin, login and create new account"):
        self.privileges = privileges

    def show_privileges(self):
        show = "The administrator is eligible to " + self.privileges
        return show


class Admin(User):
    def __init__(self, first_name,last_name,status,email):
        super().__init__(first_name,last_name,status,email)
        self.privileges = Privileges()

    
admin = Admin("Emma","Adofo","Single","emmanueladofo011@gmail.com")
print('\n')
print(admin.privileges.show_privileges())

# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you 
# used a standard dictionary to represent a glossary. Rewrite the program using 
# the OrderedDict class and make sure the order of the output matches the order 
# in which key-value pairs were added to the dictionary

from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['jen'] = 'python'
favorite_language['james'] = 'javascript'
favorite_language['micheal'] = 'ruby'
favorite_language['sandra'] = 'c'

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


glossary = OrderedDict()
glossary_count = {'tomato':'3 pieces', 'orange':'2 pieces', 'kontomire':'3 pieces'}

for name, glossary in glossary_count.items():
    print("We will need " + glossary + " of " + name.title())


# 9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the 
# range you provide. The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default 
# value of 6. Write a method called roll_die() that prints a random number 
# between 1 and the number of sides the die has. Make a 6-sided die and roll 
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint


class Die():
    def __init__(self, sides):
        self.sides = sides


    def roll_die(self):
        self.x = randint(1, self.sides)
        print(self.x)        

first_die = Die(6)
print("\nResult for first die")
for i in range(1, 10):
    first_die.roll_die()

second_die = Die(10)
print("\nResult for second die")
for i in range(1, 10):
    second_die.roll_die()