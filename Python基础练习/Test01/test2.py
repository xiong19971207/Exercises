# @Author ：Bear
# @Date   ：2020/6/26 21:15


import time


def cal_time(fn):
    def do_action():
        start = time.time()
        fn()
        end = time.time()
        result = end - start
        print('函数花费了%f秒' % result)

    return do_action


@cal_time
def d():
    for i in range(100000):
        print('Hello World!')


print(d)
