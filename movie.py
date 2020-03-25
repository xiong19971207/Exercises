while True:
    message = input('您的年龄是：')
    price = '你的价格是：'
    if message == 'quit':
        break
    try:
        age = int(message)
        if age:
            if age < 3:
                print(price + '0')
            elif 3 <= age <= 12:
                print(price + '10')
            elif age > 12:
                print(price + '15')
    except ValueError:
        print('别瞎几把输入')
