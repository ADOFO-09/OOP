import unittest 
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """Do names like Emmanuel Adofo exist """
        formatted_name = get_formatted_name("Emmanuel","Adofo")
        self.assertEqual(formatted_name, "Emmanuel Adofo")

unittest.main()