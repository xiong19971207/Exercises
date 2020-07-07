result = {}
while True:
    name = input('你叫什么名字：')
    location = input('你最想去什么地方旅游？')
    result[name] = location
    again = input('还继续吗？yes/no')
    if again == 'no':
        break
    elif again == 'yes':
        continue
    else:
        print('别瞎几把输入')
        continue

for name, location in result.items():
    print(name + '最想去%s旅游'% location)
