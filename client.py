from learn_celery import task1
from learn_celery import task2

print('start')

res1 = task1.add.delay(1, 5)
res2 = task2.multiply.delay(3, 7)

print(res1.get())  # get函数可以获取返回值
print(res2.get())

print('End')
