# 11-3. Employee: Write a class called Employee. The __init__() method should 
# take in a first name, a last name, and an annual salary, and store each of these 
# as attributes. Write a method called give_raise() that adds $5000 to the 
# annual salary by default but also accepts a different raise amount.
# Write a test case for Employee. Write two test methods, test_give_
# default_raise() and test_give_custom_raise(). Use the setUp() method so 
# you don’t have to create a new employee instance in each test method. Run 
# your test case, and make sure both tests pass

class Employee():
    def __init__(self,first_name, last_name, default_raise, annual_salary= 10000):
        self.first_name = first_name
        self.last_name = last_name
        self.default_raise = default_raise
        self.annual_salary = annual_salary

    def give_raise(self, custom_raise):
        default_salary_raise = self.annual_salary + self.default_raise
        print("The current salary is $" + str(default_salary_raise))
        self.custom_raise = custom_raise
        new_custom_salary = self.annual_salary + custom_raise
        print("The new salary is $" + str(new_custom_salary))

# emp1 = Employee("Emmanuel","Adofo", 150)
# print(emp1.give_raise())

        