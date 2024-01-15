# Handling the FileNotFoundError exception
# filename = "alice.txt"

# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print("Sorry, the file " + filename + " doesn't exist"  )


# Analysing Text
filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f_obj:
        contents = f_obj.read()
# This allows you to handle cases where the file does not exist
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " doesn't exist"
    print(msg)
# This allows you to handle cases where the file contains characters that cannot be decoded using the specified encoding
except UnicodeDecodeError:
    msg1 = "Error decoding the file " + filename + ". Please check the file encoding"
    print(msg1)
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    result = "The file " + filename + " has about " + str(num_words) + " words."
    print(result)