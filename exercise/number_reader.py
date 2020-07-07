import json

with open('number.json') as f_obj:
    numbers = json.load(f_obj)

    print(numbers)