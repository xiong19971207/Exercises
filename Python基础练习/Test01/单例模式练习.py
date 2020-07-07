# @Author ：Bear
# @Date   ：2020/6/7 20:45


class T:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            _instance = super().__new__(cls, *args, **kwargs)
            cls._instance = _instance
        return cls._instance


a = T()
b = T()

print((a == b))
