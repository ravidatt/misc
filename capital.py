import glob

class CountCapitalLetter:

    @staticmethod
    def getCountCapLetter(filename):

        with open(filename,mode='rt') as f:
            from functools import reduce
            word=reduce(lambda x,y : x+y, [int(bool(str(words).isupper())) for words in [line.split(' ') for line in iter(f.read())]])
            print(word)


    def splitFile(self):
        with open('storyline', mode='rt',buffering=1) as f:
            count=0
            lines=50000
            fileCount=0
            file = open("storyline_" + str(fileCount), mode='wt',buffering=1)
            for line in f:
                if(count>0 and count%lines==0):
                  file.flush()
                  file.close()
                  fileCount+=1
                  file=open("storyline_"+str(fileCount),mode='wt',buffering=1)
                  count=0
                  lines=50000
                  file.write(line)
                  count+=1

                file.write(line)
                count += 1

            file.flush()
            file.close()

    def readSplitFiles(self):
        files=glob.glob('storyline_*')
        for name in files:
            CountCapitalLetter.getCountCapLetter(name)



c=CountCapitalLetter()
c.splitFile()
c.readSplitFiles()

