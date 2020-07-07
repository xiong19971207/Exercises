import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


# 创建一个叫Card的类，后面是一个字符串序列

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))

print(deck[2])
print(choice(deck))


