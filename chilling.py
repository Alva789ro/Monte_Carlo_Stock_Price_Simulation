import pandas_datareader.data as dtr
import datetime as dt
import pandas as pd
import numpy
import re

#msft = dtr.DataReader('MSFt', 'iex')
#print()
lis2= ['Missing_1', 'Missing_10']
findall_r = re.findall(r'\t(\d+.\d+)', '2/2/2012 16:00:00\t26.57' )
print(findall_r)
lis2[0]='fu'
print(lis2)



'''
list_1=[]
    list_of_indexes = []
    for x in readings:
        findall_r = re.findall(r'(Missing_\d+)', x)
                if findall_r != []:
            list_1.append(findall_r)
'''

print(round(2.3234, 2))

if 7 >= 0:
    print('yes')

#import pandas as pd

def calculateRatio(stdin):
    stdin = pd.DataFrame(stdin)
    nu_mcaps, dolla_rper, ban_gper, mone_yper, n00_0per, mak_eper = df.mean(axis = 0)
    ratio = (dolla_rper + ban_gper) / (mone_yper + n00_0per + mak_eper)
    norm_ratio = (ratio + nu_mcaps)/ nu_mcaps
    return round(norm_ratio, 4)

calculateRatio()
