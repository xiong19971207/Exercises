# @Author ：Bear
# @Date   ：2020/6/16 17:35


def cal_time(fn):
    print('cal_time被调用了,内存地址是===>{}'.format(cal_time))

    def do_action():
        fn()
        print(fn)
    return do_action


@cal_time
def test():
    print("Hello World")


test()
