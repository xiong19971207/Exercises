def add_ingredients(*toppings):
    print('你的三明治中添加了以下食材：', end='')
    for i in toppings:
        print(i, end=' ')
    print()


add_ingredients('a')
add_ingredients('a', 'b')
add_ingredients('a', 'd', 'd')
