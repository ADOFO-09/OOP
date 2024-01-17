import json

filename = 'StoringData (json)/numbers.json'
# The file is opened in read mode
with open(filename) as f_obj:
    # Json.load() loads information stored in numbers.json
    numbers = json.load(f_obj)

print(numbers)