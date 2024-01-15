# Exception handling
# print(50/0)

# Using the try except block to catch error
try:
    print(50/0)
except ZeroDivisionError:
    print("You can't divide by zero")

# Using exceptions to prevent crashes
print("Give me two numbers, I will divide them")
print("Enter q to quit")

while True:
    first_number = input("Enter first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    if second_number == 'q':
        break
    
    answer = int(first_number) / int(second_number)
    print(answer)

# Using the try-except-else block
print("Give me two numbers, I will divide them")
print("Enter q to quit")

while True:
    first_number = input("Enter first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else: 
        print(answer)
