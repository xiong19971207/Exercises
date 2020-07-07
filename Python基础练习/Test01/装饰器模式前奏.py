# @Author ：Bear
# @Date   ：2020/6/16 11:24

import time


def a():
    for i in range(100000):
        print(i)


def b():
    for i in range(1000000):
        print('Hello World!')


def cal_time(fn):
    # 计算时间
    start = time.time()
    fn()
    end = time.time()
    print(end - start)
