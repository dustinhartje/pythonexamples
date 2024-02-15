# Various bits and bobs around classes and complex objects
# Loosely based on some work done for dhcharts.py in my backtesting project
# but way oversimplifying

from datetime import datetime as dt
import time

class Candle(object):
    def __init__(self, c_datetime):
        self.c_datetime = c_datetime


class Chart(object):
    def __init__(self,
            # NOTE - Python does not create a new empty list if we use:
            #        candles: list = []
            #        here... it points to the previously created list from
            #        any prior instance and keeps appending it resulting in
            #        incorrect behavior.  Instead we need to set it to None...
            candles: list = None):
        # ... and use this logic to get the desired result as a default
        # or passed value
        if candles is None:
            self.candles = []
        else:
            self.candles = candles

    def sort_candles(self):
        self.candles.sort(key=lambda c: c.c_datetime)

# Create a few objects to play with

print('\nCreating 3 candles 1 second apart, one moment please')
print('creating c1')
c1 = Candle(dt.now())
time.sleep(1)
print('creating c2')
c2 = Candle(dt.now())
time.sleep(1)
print('creating c3')
c3 = Candle(dt.now())
time.sleep(1)

chart = Chart([c2, c3, c1])

# Play!

print('\nSort a list within a class instance')
print('\nList of Candles in Chart starts out of order (note secs(ms) in last attribute')
for c in chart.candles:
    print(vars(c))
print('\nWe can sort them in place by c_datetime')
chart.sort_candles()
for c in chart.candles:
    print(vars(c))

# Reading and Writing objects to files as json:
# ...see json.py in this repo
