a = [8, 9, 4, 2, 6, 7, 1, 3, 0, 5]


def _sort(_list):
    for i in range(len(_list) - 1):
        for j in range(len(_list) - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
    return _list


def sort1(_list):
    for i in range(len(_list) - 1):
        for j in range(len(_list) - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
    return _list


print(sort1(a))
