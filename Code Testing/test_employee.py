import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
# This method creates an employee instance
    def setUp(self):
        self.employee = Employee("Emmanuel","Adofo")   

# This method tests for default_raise in salary
    def test_give_default_raise(self):
       self.employee.give_raise()
       expected_salary = self.employee.default_raise + 8000
       self.assertEqual(self.employee.annual_salary, expected_salary)

# This method tests for custom raise in salary
    def test_give_custom_raise(self):
        custom_raise = 5000
        self.employee.give_raise()
        expected_salary =  5000 + custom_raise
        self.assertEqual(self.employee.annual_salary, expected_salary)  

unittest.main()         

