import functools
from enum import Enum, unique
import os


class Fib(object):

    def __init__(self):
        self.a = 0
        self.b = 1

    def __str__(self):
        return 'this is a Fib instance.'

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.b > 10000000:
            raise StopIteration
        return self.b

    def __getitem__(self, item):
        if isinstance(item, int):
            res = 0
            for i in range(item):
                res = self.__next__()
            return res
        elif isinstance(item, slice):
            res = []
            if item.step is None or item.step > 0:
                if item.step is None:
                    step = 1
                else:
                    step = item.step
                if item.start > item.stop:
                    raise ValueError('Wrong slice.')
                for i in range(item.start):
                    self.__next__()
                for i in range(0, item.stop - item.start, step):
                    res.append(self.__next__())
                return res
            else:
                if item.stop > item.start:
                    raise ValueError('Wrong slice.')
                for i in range(item.stop):
                    self.__next__()
                for i in range(0, item.start - item.stop, -item.step):
                    res.append(self.__next__())
                res.reverse()
                return res


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.char = characters
        self.index = [i for i in range(combinationLength)]
        self.first_time = True

    def next(self) -> str:
        if self.index[-1] == len(self.index) - 1 and self.first_time:
            self.first_time = False
            return self.char[:len(self.char) - 1]
        i = 0
        while self.index[-1 - i] == len(self.char) - 1 - i:
            i += 1
        self.index[-1 - i] += 1
        start = self.index[-1 - i] + 1
        for j in range(len(self.index) - 1 - i + 1, len(self.index)):
            self.index[j] = start
            start += 1
        res = ''.join(list(map(lambda x: self.char[x], self.index)))
        return res

    def hasNext(self) -> bool:
        return not self.index[0] == len(self.char) - len(self.index)


if __name__ == '__main__':
    o = CombinationIterator('abc', 2)
    while o.hasNext():
        print(o.next())




