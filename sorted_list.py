class SimpleList:

    def __init__(self,items=[]):
        self._items=items

    def add(self,item):
        print(' add of SimpleList')
        self._items.append(item)

    def sort(self):
        self._items.sort()

    def __str__(self):
        return ' SimpleList {}'.format(self._items)

    def __repr__(self):
        return 'SimpleList {} '.format(self._items)

    def __len__(self):
        return len(self._items)

class SortedList(SimpleList):
    def __init__(self,items=()):
        super().__init__(items)
        self.sort()

    def add(self,item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self._items))

class IntList(SimpleList):
    def __init__(self,items=()):
        for x in items:IntList._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(item):
        if not isinstance(item,int):
            raise TypeError('IntList only supports integer values.')
        return True

    def add(self,item):
        IntList._validate(item)
        super().add(item)

    def __repr__(self):
        return 'IntList {}'.format(self._items)

class SortedIntList(IntList, SortedList):



    def __repr__(self):
        return 'SortedIntList({!r})'.format(self._items)

print(SortedIntList.mro())
sil=SortedIntList([2,23,23,4,435,54])
sil.add(10)
print(repr(sil))