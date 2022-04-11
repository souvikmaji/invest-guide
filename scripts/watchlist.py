import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from datetime import date, timedelta
from email_sending import Notifier

ghcl = yf.Ticker('GHCL.NS')
start_date = date(2020,8,31)
end_date = date.today() + timedelta(days=1)

ghcl_df = ghcl.history(start=start_date, end=end_date)
ghcl_df.ta.supertrend(period=10, multiplier=3, append = True)

if ghcl_df.iloc[[-1]]['SUPERTd_7_3.0'][0] == -1:
    msg = f'super trend reversed. sell\n{ghcl_df.iloc[[-1]].to_string()}'
    print(msg)
    notifier = Notifier()
    notifier.notify('SELL STOCK: GHCL', msg)
else:
    print(f'hold ghcl\n{ghcl_df.iloc[[-1]].to_string()}')