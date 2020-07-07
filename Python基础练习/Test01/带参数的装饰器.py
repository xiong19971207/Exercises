# @Author ：Bear
# @Date   ：2020/6/18 16:14


def outer(clock):
    print('outer被调用了')

    def wraper(fn):
        print(fn)
        print(wraper)
        print('wraper被调用了')

        def inner(name, game):
            print(inner)
            print(fn)
            print('inner被调用了')

            if clock < 22:
                fn(name, game)
            else:
                print('太晚了，别玩了')

        return inner

    return wraper


@outer(22)
def play_game(name, game):
    print(name + '在玩儿' + game)


# play_game('zs', '刺激')
print(play_game)