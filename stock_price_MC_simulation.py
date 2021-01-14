import pandas_datareader.data as dtr
import datetime as dt
import pandas as pd
import numpy
start = dt.datetime(2020, 8, 9)
end = dt.datetime(2020, 12, 9)

#prices = dtr.DataReader('AAPL','iex' , start, end)['Close']
#appl= dtr.DataReader('APPL', 'iex')
for x in range(1, 51):
    if x % 3 == 0 and x % 5 == 0:
        x = 'buzzfizz'
        print(x)
    elif x % 3 == 0:
        x = 'fizz'
        print(x)
    elif x % 5 == 0:
        x = 'buzz'
        print(x)
    else:
        print(x)


if 1 > 2 or 1 > 3:
    print('no')
else:
    print('what')


print((27.47 + 27.728+ 28.19+ 28.1+ 28.15)/5)
