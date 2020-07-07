# @Author ：Bear
# @Date   ：2020/6/18 15:14


import time


def cal_time(fn):
    def do_action(x,y):
        start = time.time()
        fn(x,y)
        end = time.time()
        print(end - start)

    return do_action


@cal_time
def aaa(x,y):
    for i in range(100000):
        print(x+y)


aaa(6,6)