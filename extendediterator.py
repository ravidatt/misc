class ExtIteratorDemo:

    def read_file_till_end(self):
        FILE_NAME = 'storyline'
        with open(FILE_NAME,mode='rt') as f:
            for line in iter(lambda : f.readline().strip(),'End'):
                print(line)

e = ExtIteratorDemo()
e.read_file_till_end()