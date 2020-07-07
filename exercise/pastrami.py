
sandwich_orders = ['a', 'b', 'c', 'd', 'pa', 'pa', 'pa']

print('pa卖完了')
while 'pa' in sandwich_orders:
    sandwich_orders.remove('pa')
print(sandwich_orders)