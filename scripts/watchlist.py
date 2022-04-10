import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from datetime import date
from email_sending import Notifier


ghcl = yf.Ticker('GHCL.NS')
start_date = date(2020,8,31)
end_date = date.today()

ghcl_df = ghcl.history(start=start_date, end=end_date)
ghcl_df.ta.supertrend(period=10, multiplier=3, append = True)

if ghcl_df.iloc[[-1]]['SUPERTd_7_3.0'][0] == -1:
    print('super trend reversed. sell')
    notifier = Notifier()
    notifier.notify('SELL STOCK: GHCL', 'Super trend reversed. time to sell ghcl')
else:
    print('hold ghcl')