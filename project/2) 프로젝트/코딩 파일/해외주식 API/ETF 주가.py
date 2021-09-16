from pandas_datareader import data

ETF = data.DataReader(['IYK','IXN','IBUY','PBS','PJP','SOXX','RTH','MJ','FTXG', 'IYK', 'XLC'],'yahoo','2019-08-02','2021-08-31')

print(ETF['Adj Close'])

ETF.to_csv("./ETF_price.csv")