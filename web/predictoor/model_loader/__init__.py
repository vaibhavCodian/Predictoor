from flask import url_for
from predictoor import app
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from matplotlib import style
# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__
# Adjusting the style of matplotlib
style.use('ggplot')


def stock_l(ticker):
    plt.clf()
    #--> Getting Data
    # We would like all available data from 10 month back (approx ~) 
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=(30 * 10))
    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    df = data.DataReader('AAPL', 'yahoo', start_date, end_date)
    # Preprocessing Days and Setting labels
    close = df['Close']
    close_px = df['Adj Close']
    mavg = close_px.rolling(window=100).mean()
    all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
    close = close.reindex(all_weekdays)
    close = close.fillna(method='ffill')
    close_px.plot(label='AAPL')
    mavg.plot(label='mavg')
    plt.legend()
    # Saving
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)  # rewind to beginning of file
    figdata_png = figfile.getvalue()  # extract string (stream of bytes)
    figdata_png = base64.b64encode(figdata_png)
    return figdata_png


