# Try It Yourself
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an 
# instance called restaurant from this class. Print the number of customers the 
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number 
# of customers that have been served. Call this method with a new number and 
# print the value again.
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a 
# day of business.

#9-4
class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def read_customers(self):
        print("The total number of customers served today is " + str(self.number_served))
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, overflow):
        self.number_served += overflow

restaurant = Restaurant('Anita restaurant', 'Foreign cousines')
restaurant.set_number_served(30)
restaurant.increment_number_served(100)
restaurant.read_customers()


# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write 
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts(). Print login_attempts again to 
# make sure it was reset to 0

class User():
    def __init__(self, first_name,last_name,status,email):
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.email = email
        self.login_attempts = 0
    def describe_user(self):
        print("Your first name is " + self.first_name + " and your last name is " + self.last_name + "\nRelationship status: " + self.status + "\nEmail: " + self.email)
    def greet_user(self):
        print("Welcome to your profile")
        # Modifying an attribute through a method call
    def increment_login_attempts(self, entry):
        self.login_attempts += entry
        print("Your current entry count is " + str(self.login_attempts))
    def reset_login_attempts(self, signout):
        self.login_attempts -= signout
        print("Your current entry count is " + str(self.login_attempts))

new_user = User("Emmanuel","Adofo","Single","emmanuel@gmail.com")
new_user.greet_user()
new_user.describe_user()
new_user.increment_login_attempts(1)
new_user.reset_login_attempts(1)



