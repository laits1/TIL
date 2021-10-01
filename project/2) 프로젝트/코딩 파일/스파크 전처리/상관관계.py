import inline as inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

import quandl
quandl.ApiConfig.api_key = 'zbUxxzuDxrACyfheY6o9'

stocks = ['MSFT', 'AMD', 'AMZN', 'KO','MCD','MO','NKE','PFE','WMT'] #SPOT, FB, TSLA
benchmarks = ['SPY', 'SHV']
data = {}
for s in stocks + benchmarks:
    data[s] = quandl.get("EOD/"+s)

prc = pd.DataFrame()

for s in stocks + benchmarks:
    tmp = data[s][['Adj_Close']]
    tmp.columns = [s]
    prc = pd.concat([prc, tmp], axis=1)
    prc = prc[prc.index.weekday < 5]

prc = prc.dropna()

portfolio = prc[['MSFT', 'AMD', 'AMZN', 'KO','MCD','MO','NKE','PFE','WMT','SPY','SHV']]
portfolio = prc[['MSFT', 'AMD', 'AMZN', 'KO', 'MCD', 'MO', 'NKE', 'PFE', 'WMT','SPY','SHV']].pct_change()
portfolio_data = 1 +  portfolio
portfolio_data.loc[pd.to_datetime("2007-01-11")] = 1
portfolio_data = portfolio_data.sort_index()

portfolio_data = portfolio_data.cumprod()
portfolio_data.to_csv('./daily.csv')
portfolio['SPY'].to_csv('./SPY.csv')
portfolio['SHV'].to_csv('./SHV.csv')