# @Author ：Bear
# @Date   ：2020/6/16 11:45


import time


# 简单装饰器
def cal_time(fn):
    print(fn)

    def do_action():
        start = time.time()
        fn()
        end = time.time()
        print('函数执行花费了%f秒' % (end - start))

    return do_action


@cal_time(100)
def test():
    for i in range(100000):
        print(i)

test
