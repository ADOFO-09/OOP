# Saving and reading user generated data
import json

username = input("Enter your name: ")

filename = 'StoringData (json)/username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We will remember you when you come back " + username + "!")