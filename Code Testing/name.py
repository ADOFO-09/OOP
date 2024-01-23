from name_function import get_formatted_name

print("Enter 'q' to quit")
while True:
    first = input("Enter first name:")
    if first == 'q':
        break
    last = input("Enter second name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name)

