import unittest
from city_functions import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Does a city and a country like Kumasi Ghana exist?"""
# The method below tests for a city and a country
    def test_city_country(self):
        formatted_name = get_formatted_name('kumasi', 'ghana')
        self.assertEqual(formatted_name, 'kumasi, ghana')
        
# The method below test for a city, a country and population
    def test_city_country_population(self):
        formatted_name = get_formatted_name('santiago', 'chile', 'population=5000000')
        self.assertEqual(formatted_name, 'santiago, chile and population=5000000')

unittest.main()