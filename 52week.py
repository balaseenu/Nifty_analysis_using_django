import os
import pandas as pd
from stock_name import get_200nsedata
from stock_details import get_histdata
from datetime import datetime, timedelta


def get_52weeks():
    startdate = datetime.today() - timedelta(365)
    enddate = datetime.today()
    interval = '1d'

    symbol = get_200nsedata()
    out = get_histdata(symbol, startdate, enddate, interval)

def get_52week_calculation(percent):
    for filename in os.listdir('datasets/monthly'):
        week52 = pd.read_csv('datasets/monthly/{}'.format(filename))
        high = week52['Close'].head(1)
        low = week52['Close'].tail(1)
        range_down = low * percent
        range_up = ((low - range_down) + low)
        high = int(high)
        low = int(low)
        range_down = int(range_down)
        range_up = int(range_up)
        uptrend = []
        downtrend = []
        if high < low and range_up < high:
            print('the uptrening stocks are : {}'.format(filename))
            uptrend.append(filename)
        elif high > low:
            print('the downtrening stocks are : {}'.format(filename))
            downtrend.append(filename)
    return uptrend, downtrend

user_input = int(input('enter the percentage : '))
percent = (100 - user_input) / 100

if __name__ =='__main__':
#    print(get_52weeks())
     up,down = get_52week_calculation(percent)
     print('the uptrening stocks are : {}'.format(up))
     print('the downtrening stocks are : {}'.format(down))
