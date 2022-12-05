import pandas as pd

def get_200nsedata():
    data = pd.read_csv('ind_nifty200.csv')
    nse_200data = data['Symbol'].to_list()
    return nse_200data

def get_50nsedata():
    data = pd.read_csv('ind_nifty50.csv')
    nse_50data = data['Symbol'].to_list()
    nse_50data = nse_50data[1:]
    return nse_50data

if __name__ == '__main__':
    print(get_50nsedata())
    print(get_200nsedata())