# # relative file path
# with open('text_file/pi_digits.txt') as object_file:
#     contents = object_file.read()
#     print(contents.rstrip())


# # absolute file path
# file_path = 'D:/other_files/2pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# # reading file line by line
# filename = 'pi_digits.txt'

# with open(filename) as new_object:
#     for line in new_object:
#         print(line.rstrip())

# Making a list of lines from a file
file1name = 'pi_digits.txt'

with open(file1name) as new1_object:
    lines = new1_object.readlines()

for line in lines:
    print(line.rstrip())



