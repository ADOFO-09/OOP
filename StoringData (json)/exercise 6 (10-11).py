# 10-11. Favorite Number: Write a program that prompts for the user’s favorite 
# number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite 
# number! It’s _____.

import json

filename = "StoringData (json)/fav_number.json"
prompt = "Enter your favorite number:"
# Getting user input
fav_number = int(input(prompt))
# Responsible for storing number in a file
def keep_user_number():
    with open(filename, 'w') as file_obj:
        json.dump(fav_number, file_obj)
        return fav_number
# Responsible for retrieving stored number
def get_stored_number():
        fav_number = keep_user_number()
        with open(filename) as file_obj:
            fav_number = json.load(file_obj)
        print("I know your favorite number! It's " + str(fav_number))
    
get_stored_number()