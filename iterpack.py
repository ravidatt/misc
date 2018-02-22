from DemoMe import Demo
class Iterdemo:

    def __init__(self,index,*data):
        self._index = index
        self._data = data

    def __str__(self):
        return 'index={} data={}'.format(self._index,self._data)


cls = Iterdemo(10,[323,232,3,23,23,23,32])
dd=Demo(10,[12,3,4,34,5])
print(dd)