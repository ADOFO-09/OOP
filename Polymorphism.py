# COMPILE-TIME POLYMORPHISM
class employee1():
    def name(self):
        print("Emmanuel is my name")
    def salary(self):
        print("400 is my salary")
    def age(self):
        print("20 is my age")

class employee2():
    def name(self):
        print("Rahul is my name")
    def salary(self):
        print("330 is my salary")
    def age(self):
        print("18 is my age")

def func(obj): #Method overloading
    obj.name()
    obj.salary()
    obj.age()

obj_emp1 = employee1()
obj_emp2 = employee2()
func(obj_emp1)
func(obj_emp2)
    
# RUN-TIME POLYMORPHISM
class employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def earn(self):
        pass

class childemployee1():
    def earn(self):
        print("no money")
class childemployee2():
    def earn(self):
        print("has money")
c = childemployee1
c.earn(employee)
d = childemployee2
d.earn(employee)