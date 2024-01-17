import json

numbers = [1,2,3,4,5,6,7,8,9,10]

filename = 'StoringData (json)/numbers.json'
# The file is opened in write mode 
with open(filename, 'w') as f_obj:
    # json.dump takes two arguments: a piece of data to store and file object it will use to store.
    json.dump(numbers,f_obj)

