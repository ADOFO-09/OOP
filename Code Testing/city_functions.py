# City, Country: Write a function that accepts two parameters: a city name 
# and a country name. The function should return a single string of the form 
# City, Country, such as Santiago, Chile. Store the function in a module called 
# city_functions.py.
# Create a file called test_cities.py that tests the function you just wrote 
# (remember that you need to import unittest and the function you want to test).
# Write a method called test_city_country() to verify that calling your function 
# with values such as 'santiago' and 'chile' results in the correct string. Run 
# test_cities.py, and make sure test_city_country() passes

def get_formatted_name(city, country, population=''):
    if population:
        full_name = city + ", " + country + " and " + population
    else:
        full_name = city + ", " + country
    return full_name


# 11-2. Population: Modify your function so it requires a third parameter, 
# population. It should now return a single string of the form City, Country – 
# population xxx, such as Santiago, Chile – population 5000000. Run 
# test_cities.py again. Make sure test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run 
# test_cities.py again, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies you can call your function with the values 'santiago', 'chile', and 
# 'population=5000000'. Run test_cities.py again, and make sure this new test 
# passes

