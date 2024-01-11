# class employee():
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary

# emp1 = employee("Adofo",12,2,400)
# emp2 = employee("Emmanuel",45,67,500)
# print(emp1.__dict__)

#SINGLE INHERITANCE
# class employee(): #Parent class
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary
# class childemployee(employee): #Child class
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary

# emp1 = employee("Adofo",12,2,400)
# emp2 = employee("Emmanuel",45,67,500)
# print(emp1.age)
# print(emp2.name)

#MULTILEVEL INHERITANCE
class employee(): #Supper class
    def __init__(self,name,age,id,salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
class childemployee1(employee): #First child class
    def __init__(self,name,age,id,salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
class childemployee2(childemployee1): #Second child class
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

emp1 = employee("Adofo",12,2,400)
emp2 = childemployee1("Emmanuel",45,67,500)
print(emp1.age)
print(emp2.id)

#HIERARCHICAL INHERITANCE
# class employee(): #Hierarchical class
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary
# class childemployee1(employee): #First child class
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary
# class childemployee2(employee): #Second child class
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary

# emp1 = employee("Adofo",12,2,400)
# emp2 = employee("Emmanuel",45,67,500)
# print(emp1.age)
# print(emp2.age)

#MULTIPLE INHERITANCE
# class employee1(): # Parent class
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary
# class employee2(): # Parent class
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary
# class childemployee2(employee1, employee2): # child class inheriting from more than one base class
#     def __init__(self,name,age,id,salary):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.salary = salary

# emp1 = employee1("Adofo",12,2,400)
# emp2 = employee2("Emmanuel",45,3,500)
# print(emp1.id)
# print(emp2.id)