import random
import datetime
import itertools
import time


class Sensor:


    def __init__(self):
       print(' initilized Sensor')

    def __iter__(self):
        return self

    def __next__(self):
        return random.random()

s=Sensor()
timestamps=iter(datetime.datetime.now,None)
for stamp, value in itertools.islice(zip(timestamps, s),):
    print(stamp, value)
    time.sleep(5)
