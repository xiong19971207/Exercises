import json

numbers = [5, 8, 9, 8, 7, 1, 5]

with open('number.json', 'w') as f_obj:
    json.dump(numbers, f_obj)
