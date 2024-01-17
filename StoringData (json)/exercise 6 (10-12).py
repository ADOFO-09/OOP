# 10-12. Favorite Number Remembered: Combine the two programs from 
# Exercise 10-11 into one file. If the number is already stored, report the favorite 
# number to the user. If not, prompt for the user’s favorite number and store it in a 
# file. Run the program twice to see that it works

import json

filename = "StoringData (json)/fav_number.json"
prompt = "Enter your favorite number: "
try:
    with open(filename) as f_obj:
        fav_number = json.load(f_obj)
        
except (FileNotFoundError, json.JSONDecodeError):
        try:
            fav_number = int(input(prompt))
        except ValueError:
            print("Invalid literal, please enter a number")
        else:
            with open(filename, 'w') as f_obj:
                json.dump(fav_number, f_obj)
                msg = "Your favorite number will be remembered"
                msg += " when you come back! it's " + str(fav_number)
                print(msg)
        
else:
    print("Your favorite number is "+ str(fav_number))