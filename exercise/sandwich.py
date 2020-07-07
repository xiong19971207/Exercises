
sandwich_orders = ['a', 'b', 'c', 'd']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('三明治%s正在制作中。。。' % sandwich)
    finished_sandwiches.append(sandwich)

print('你的三明治全在这：', end=' ')
for i in finished_sandwiches:
    print(i, end=' ')

