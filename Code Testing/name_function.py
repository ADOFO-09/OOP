def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted name"""
# Responsible for formatting names with middle name
    if middle:
        full_name = first + ' ' + middle + ' ' + last

# Responsible for formatting names with a first and last name
    else:
        full_name = first + ' ' + last
    return full_name.title()


# In response to a failed test, don't change the test. Instead
# fix the code that caused the test to fail.