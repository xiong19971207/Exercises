# 一个类只有一个实例
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            _instance = super().__new__(cls, *args, **kwargs)
            cls._instance = _instance
        return cls._instance


class Myclass(Singleton):
    pass


a = Myclass()
b = Myclass()

print(id(a))
print(id(b))

print(a is b)