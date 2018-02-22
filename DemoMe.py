class ExampleIterator:

    def __init__(self,data):
        self._index=0
        self._data=data

    def __str__(self):
        return '{} {}'.format(self._index,self._data)

    def __repr__(self):
        return 'index={} data={}'.format(self._index, self._data)

    def __iter__(self):
        return self

    x= lambda x : x+1

    def __next__(self):
        if self._index == len(self._data):
            raise StopIteration()
        r = self._data[self._index]
        self._index+=1
        return r

class ExampleIterable:
    def __init__(self, data):
        self._data=data

    def __iter__(self):
        return ExampleIterator(self._data)

class AlternateIterable:
    def __init__(self):
        self.data=[1,2,3,4,5,6]

    def __getitem__(self, item):
        return self.data[item]


i=ExampleIterable([1,2,3,4,5,6])
for x in i:
    print(x)
print([xx*10 for xx in i])

print([jj for jj in AlternateIterable()])


