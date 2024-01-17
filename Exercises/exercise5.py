# 10-6. Addition: One common problem when prompting for numerical input 
# occurs when people provide text instead of numbers. When you try to convert 
# the input to an int, you’ll get a TypeError. Write a program that prompts for 
# two numbers. Add them together and print the result. Catch the TypeError if 
# either input value is not a number, and print a friendly error message. Test your 
# program by entering two numbers and then by entering some text instead of a 
# number

try:
    prompt = "Enter number: "
    first_number = int(input(prompt))
    second_number = int(input(prompt))
except ValueError:
    print("Invalid literal, please enter a number")
else:
    result = first_number + second_number
    print(result)

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop 
# so the user can continue entering numbers even if they make a mistake and 
# enter text instead of a number
    
# while True:
#     try:
#         prompt = "Enter number: "
#         first_number = int(input(prompt))
#         second_number = int(input(prompt))
#     except ValueError:
#         print("Invalid literal, please enter a number")
#     else:
#         result = first_number + second_number
#         print(result)

# line = "Row, row, row your boat"
# # lower() catches all appearances of the word 
# result = line.lower().count("row")
# print(result)

# 10-10. Common Words: Write a program that reads the files you found at Project Gutenberg and 
# determines how many times the word 'the' appears in each text
def times_count(filename):
    try:
        with open(filename, encoding = 'utf-8') as file_obj:
            lines = file_obj.read()
            result = lines.lower().count('the')
            print("The word 'the' appears in " + filename +" "+ str(result) + " times.")
    except FileNotFoundError:
        print("Sorry the file " + filename + " does not exist")

filenames = ['Exceptions/little.txt','Exceptions/moby.txt']
for filename in filenames:
    times_count(filename)


