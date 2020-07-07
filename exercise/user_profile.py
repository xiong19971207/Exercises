def make_car(manufacturer, cartype, **kwargs):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['cartype'] = cartype
    for key, value in kwargs.items():
        car_info[key] = value
    print(car_info)
    return car_info


car = make_car('s', 'o', color='blue', two_package=True)
print(bool(''))