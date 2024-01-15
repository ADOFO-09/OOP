# Function that counts words in a file
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f_obj:
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

filename = "Exceptions/alice.txt"
count_words(filename)

# Working with Multiple files
# Using a loop to count the words in any text we want to analyze
filenames = ['Exceptions/alice.txt', 'Exceptions/little.txt','Exceptions/moby.txt','sidd.txt']
for filename in filenames:
    count_words(filename)


# Sometimes there is no need to report every exception you catch.
# Sometimes you would want the program to fail silently and continue to execution as if nothing happened
# Failing Silently
def word_count(filename):
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    # This allows you to handle cases where the file does not exist
    except FileNotFoundError:
       pass # It is a reminder that nothing is done at a specific point during program execution
       
       # The code below writes any missing filenames to a file called missing_file.txt
       with open('Exceptions/missing_files.txt', 'a') as note_obj:
           note_obj.write(filename +"\n")
           
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

filenames =  ['Exceptions/alice.txt', 'Exceptions/little.txt','moby.txt','Exceptions/sidd.txt']
for filename in filenames:
    word_count(filename)