import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):   
    
    def test_give_default_raise(self):
       self.employee = Employee("Emmanuel","Adofo", 5000)
       self.employee.give_raise()
       expected_salary = self.employee.default_raise + 5000
       self.assertEqual(self.employee.annual_salary, expected_salary)

    def test_give_default_raise(self):
        self.employee = Employee("Emmanuel", "Adofo", 5000)
        custom_raise = 5000
        self.employee.give_raise(custom_raise)
        expected_salary =  5000 + custom_raise
        self.assertEqual(self.employee.annual_salary, expected_salary)  

unittest.main()         

