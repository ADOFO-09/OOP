# Try It Yourself
# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# 9-1
class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Welcome to " + self.name + ": We offer " + self.cuisine_type)
    def open_restaurant(self):
        print("The Restaurant is open")

restaurant = Restaurant('jofel', 'french cousine')
print("The name of the Restaurant is " + restaurant.name.title())
print("We offer cousine types such as: " +restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.
print('\n...................')
# 9-2
restaurant1 = Restaurant('mama adiza', 'local cousine')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('Daavi', 'gobe cousine')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('garden city', 'jollof cousine')
restaurant3.describe_restaurant()

# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods 
# for each user
print("\n..........................")
class User():
    def __init__(self, first_name,last_name,status,email):
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.email = email
    def describe_user(self):
        print("Your first name is " + self.first_name + " and your last name is " + self.last_name + "\nRelationship status: " + self.status + "\nEmail: " + self.email)
    def greet_user(self):
        print("Welcome To Your Profile")

user1 = User("Emmanuel","Adofo","Single","emmanuel@gmail.com")
user1.greet_user()
user1.describe_user()

print('\n')
user2 = User("Yussif","Mensah","Dating","mensah@gmail.com")
user2.greet_user()
user2.describe_user()

print('\n')
user3 = User("Michael","Angelo","Dating","michael@gmail.com")
user3.greet_user()
user3.describe_user()
