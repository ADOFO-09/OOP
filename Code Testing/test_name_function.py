import unittest 
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
# The method below tests for two names that is first and last names
    def test_first_last_name(self):
        """Do names like 'Emmanuel Adofo' exist """
        formatted_name = get_formatted_name('emmanuel','adofo')
        self.assertEqual(formatted_name, 'Emmanuel Adofo')
    
# The method below tests for three names that are first last and middle
    def test_first_last_middle_name(self):
        """Do name like 'Asante Mensah Yussif' works"""
        formatted_name = get_formatted_name('asante','yussif','mensah')
        self.assertEqual(formatted_name, 'Asante Mensah Yussif')

unittest.main()



