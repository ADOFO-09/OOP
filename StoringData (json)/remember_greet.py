import json

# Load the username if it has been stored previously
# Otherwise, prompt for the username and store it
filename = 'StoringData (json)/username.json'
try:
    with open(filename) as f_obj:
        # Attempt to load the "username" from JSON file
        username = json.load(f_obj)
except (FileNotFoundError, json.JSONDecodeError):
    # Handles the case where the file is empty or doesn't exist
    username = input("What is your name:")
    with open(filename, 'w') as f_obj:
    # Writes username to JSON file
        json.dump(username, f_obj)
        print("We will remember you when you come back " + username + "!")
else:
    print("Welcome back " + username + "!")
