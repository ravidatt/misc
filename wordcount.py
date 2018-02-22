from operator import itemgetter
from collections import defaultdict
class WordCount:

    @staticmethod
    def readfromfile():
        FILE_NAME = 'storyline'
        with open(FILE_NAME, mode='rt') as f:
            V = [word for word in [line.split(' ') for line in f]][0]
        return V



    def mapper(self,word):
        alphaword=''.join(c.lower() if c.isalpha() else ' ' for c in word)
        freq ={}
        freq[word]=freq.get(alphaword,0)+1
        return freq



V=WordCount.readfromfile()
wc=WordCount()
vv=map(wc.mapper,V)
print(list(vv))