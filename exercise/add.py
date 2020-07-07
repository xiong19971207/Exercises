while True:
    try:
        num1 = int(input('输入第一个数字:'))
        num2 = int(input('输入第二个数字:'))
    except ValueError:
        print('不对')
        continue
    else:
        print(num1 + num2)
        break
