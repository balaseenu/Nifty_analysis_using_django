import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

def get_histdata(ticker, startdate, enddate, interval):
    tickk = ["{}.ns".format(tick) for tick in ticker]
    for line in tickk:
        symbol = line.split(",")[0]
        data = yf.download(symbol, start=startdate, end=enddate, interval=interval)
        if interval == '1d':
            data.to_csv('C:/Users/admin/PycharmProjects/Stockproject/datasets/monthly/{}.csv'.format(symbol))
        else:
            data.to_csv('C:/Users/admin/PycharmProjects/Stockproject/datasets/daily/{}.csv'.format(symbol))
    return data

df = pd.read_csv('ind_nifty200.csv')
ticker = df['Symbol'].to_list()
startdate = datetime.today() - timedelta(25)
enddate = datetime.today()
interval = '1h'

if __name__ == '__main__':
    get_histdata(ticker, startdate, enddate, interval)