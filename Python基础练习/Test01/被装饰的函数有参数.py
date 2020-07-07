# @Author ：Bear
# @Date   ：2020/6/16 17:49


def play_game(fn):
    print('play_game被调用了')

    def do_action(name, game):
        print('do_action被调用了')
        fn(name,game)

    return do_action


@play_game
def play(name, game):
    print('{}正在玩儿{}'.format(name, game))


play('我','吃鸡')
