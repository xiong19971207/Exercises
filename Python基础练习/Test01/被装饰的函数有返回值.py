# @Author ：Bear
# @Date   ：2020/6/18 15:25


def cal(fn):
    print('我被调用了')

    def test(x, y):
        result = fn(x, y)
        return result

    return test


@cal
def add(x, y):
    return x + y


print(add(1, 2))
