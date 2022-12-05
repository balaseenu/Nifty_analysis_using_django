import os
import pandas as pd
import matplotlib.pyplot as plt
from stock_name import get_200nsedata
from stock_details import get_histdata
from datetime import datetime, timedelta

class Volume():
    def get_data(self, cycle, interval):
        if interval[-1] == 'm':
            interval_val = int(interval[0])
            diff = round(((cycle * interval_val) / 60))
            startdate = datetime.today() - timedelta(hours=diff)
            enddate = datetime.today()
        elif interval[-1] == 'd':
            startdate = datetime.today() - timedelta(interval[0])
            enddate = datetime.today()

        symbol = get_200nsedata()
        out = get_histdata(symbol, startdate, enddate, interval)

    def volume_analysis(self, interval):
        if interval[-1] == 'm' or interval[-1] == 'h':
            for filename in os.listdir('datasets/daily'):
                week52 = pd.read_csv('datasets/daily/{}'.format(filename))
                file = filename
                v.Volume_calc(week52,file)
        else:
            for filename in os.listdir('datasets/monthly'):
                week52 = pd.read_csv('datasets/monthly/{}'.format(filename))

    def Volume_calc(self,week52,file):
        for val in range (0, len(week52['Volume'])):
            print('the value is ', val)
            hell = len(week52['Volume']) - 2
            print(week52['Volume'][hell])
            if ((week52['Volume'][hell]) > (week52['Volume'][val])):
                do
            print('the uptrening stocks are : {}'.format(file))










if __name__ == '__main__':

    cycle = int(input('Enter the number of volumes : '))
    interval = str(input('Enter the time interval : '))
    v.get_data(cycle, interval)
    v.volume_analysis(interval)
