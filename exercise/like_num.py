import json

try:
    with open('num.json') as x:
        num = json.load(x)
        print('你最爱的数字是：' + num)
except FileNotFoundError:
    num = input('输入你最喜欢的数字：\n')
    with open('num.json', 'w') as x:
        json.dump(num, x)
