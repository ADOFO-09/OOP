import json

# Responsible for retrieving stored username if one exists
def get_stored_username():
    """Get stored username if available"""
    filename = 'StoringData (json)/username.json'
    with open(filename) as f_obj:
        username = json.load(f_obj)
        checker = input("Is this username: " + username + " your name? (true/false)\n")
# Responsible for checking username if the current user is not the one who last used the program
    if checker == 'true':
        print("Welcome back " + username + "!")
    elif checker == 'false':
        get_new_username()

# Responsible for getting new username and storing it
def get_new_username():
    """Prompt for a new username"""
    filename = 'StoringData (json)/username.json'
    username = input("What is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We will remember you when you come back "+ username + "!")


    
# Before printing a welcome back message in greet_user(), ask the user if 
# this is the correct username. If it’s not, call get_new_username() to get the correct 
# username

# Prints an appropriate message: it either welcomes back an existing user or greets a new user
def great_user():
    """Greet the user by name"""
    try:
        get_stored_username()
    except json.JSONDecodeError:
        get_new_username()
   
great_user()
