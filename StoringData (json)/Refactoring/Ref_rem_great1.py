import json

# Responsible for retrieving stored username if one exists
def get_stored_username():
    """Get stored username if available"""
    filename = 'StoringData (json)/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except (FileNotFoundError, json.JSONDecodeError):
        # Handles the case where the file is empty or doesn't exist
        return None
    else:
        return username

# Prints an appropriate message: it either welcomes back an existing user or greets a new user
# Responsible for getting new username and storing it
def great_user():
    """Greet the user by name"""
    filename = 'StoringData (json)/username.json'
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = input("What is your name?")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We will remember you when you come back "+ username + "!")

great_user()

# great_user() performs multiple tasks which is not appropriate for refactoring

        