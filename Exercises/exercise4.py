# # 10-1. Learning Python: Open a blank file in your text editor and write a few 
# # lines summarizing what you’ve learned about Python so far. Start each line 
# # with the phrase In Python you can.... Save the file as learning_python.txt in the 
# # same directory as your exercises from this chapter. Write a program that reads 
# # the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing 
# # the lines in a list and then working with them outside the with block.


# filename = 'learning_python.txt'

# with open(filename) as file_object:
#     contents = file_object.read()

# for i in range(1, 4):
#     print(contents)


# with open(filename) as object_file:
#     content = object_file.read()
#     print(content.rstrip())
#     for line in object_file:
#         print(line.strip())


# with open(filename) as note_file:
#     lines = note_file.readlines()

# for line in lines:
#     print(line)


# # 10-2. Learning C: You can use the replace() method to replace any word in a 
# # string with a different word. Here’s a quick example showing how to replace 
# # 'dog' with 'cat' in a sentence:

# with open(filename) as file_note:
#     lines = file_note.readlines()

# for line in lines:
#     modi_file = line.replace('python', 'C')
#     print(modi_file.strip())

# 10-3. Guest: Write a program that prompts the user for their name. When they 
# respond, write their name to a file called guest.txt.

# user_name = input("Enter your name: ")
# file = 'guest.txt'

# with open(file, 'w') as guest_file:
#     guest_file.write(user_name + '\n')

# 10-4. Guest Book: Write a while loop that prompts users for their name. When 
# they enter their name, print a greeting to the screen and add a line recording 
# their visit in a file called guest_book.txt. Make sure each entry appears on a 
# new line in the file

# filename = 'guest_book.txt' # file directory (relative path)
# prompt = "Enter your name: " # user input 

# # Writes title in file(guest_book) as Guests Visitation
# with open(filename, 'w') as file_object:
#     file_object.write("Guests Visitation.\n")

# #Checks the number of guests
# current_count = 1
# while current_count <= 5:
#     guest_name = input(prompt)
#     # checks for existing programme 
#     if guest_name != 'quit':
#         print("Welcome to this Seminar " + guest_name.title())
#         current_count += 1
#     # exits programme
#     if guest_name == 'quit':
#         break
#     # writes guests name to file (guest_book) by appending
#     else:
#         with open(filename, 'a') as guest_book:
#             guest_book.write(guest_name +" visited the seminar today\n")

# 10-5. Programming Poll: Write a while loop that asks people why they like 
# programming. Each time someone enters a reason, add their reason to a file 
# that stores all the responses

filename = 'response.txt'
question = "Why do you like programming? "

people_count = 1
while people_count <= 5:
    reason_Programming = input(question)
    people_count += 1

    if reason_Programming == '':
        break
    else: 
        with open(filename, 'a') as response_book:
            response_book.write(reason_Programming + "\n")