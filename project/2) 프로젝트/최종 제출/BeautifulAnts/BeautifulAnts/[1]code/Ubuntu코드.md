### ubuntu

- vim change_file_format.py

```python
import pandas as pd
import os

path = 'BeautifulAnts/data/Article_List_excel/'
file_list = os.listdir(path)
file_lists_excel = [file for file in file_list if file.endswith('.xlsx')] ## 파일명 끝이 .csv인 경우
# print(file_lists_excel)

for file_name in file_lists_excel:
    company = file_name.split('.')[0]
    globals()['{}'.format(company)] = pd.read_excel('{}{}'.format(path,file_name),  engine='openpyxl')
    globals()['{}'.format(company)] = globals()['{}'.format(company)].rename(columns=globals()['{}'.format(company)].iloc[0])
    globals()['{}'.format(company)].drop(index=0, inplace=True)
    globals()['{}'.format(company)] = globals()['{}'.format(company)][['Date', '{}'.format(company)]]

    globals()['{}'.format(company)].to_csv('BeautifulAnts/data/Article_List_csv/{}.csv'.format(company))
```

- vim ch_dateType.py

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
from pandas_datareader import data
import matplotlib.pyplot as plt
from datetime import datetime

import pandas as pd
import numpy as np

def mean(corp):
    csv = pd.read_csv('./nonescoredate/'+corp+'_scda.csv')
    csv['sent']=(csv['npos']-csv['nneg'])/csv['nwords']
    del csv['Unnamed: 0']
    del csv['nwords']
    del csv['npos']
    del csv['nneg']
    csv.columns=['date','sent']
    csv['date'] = pd.to_datetime(csv['date'])
    csv.fillna(0,inplace=True)
    
    YM=[]
    for i in csv['date']:
        YM.append(str(i)[:7])
    csv['YM'] = YM
    
    df = csv.groupby(csv['YM']).mean()
#     csv.drop(['2019-07','2021-09'], inplace=True)
    df.to_csv('{}.py'.format(corp))
  
    return csv.groupby(csv['YM']).mean()#.to_csv('./mean/'+corp+'_mean.csv')
```



- vim daily.py

```python
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
```



- vim Industrial_price.py

```python
#import packages
import pandas as pd
import quandl

quandl.ApiConfig.api_key = 'zbUxxzuDxrACyfheY6o9'
stocks = ['TSLA', 'WMT', 'MO', 'AMD', 'MSFT', 'FB', 'AMZN', 'SPOT', 'PFE', 'MCD','KO','NKE']
data = {} 
prc = pd.DataFrame()  

for stock in stocks:
    data[stock] = quandl.get("EOD/"+stock, collapse='monthly',start_date="2019-07-01", end_date="2021-08-31") 
    tmp = data[stock][['Adj_Close']]  
    tmp.columns = [stock]
    prc = pd.concat([prc, tmp], axis=1)
    
    globals()['{}'.format(stock)] = prc[['{}'.format(stock)]]
    globals()['{}'.format(stock)].to_csv('data/monthly/Industrial/{}.csv'.format(stock))
```



- vim ETF_price.py

```python
import pandas_datareader as pdr
import datetime as dt

ticker = ['IYK','IXN','IBUY','PBS','PJP','SOXX','RTH','MJ','FTXG', 'IYK', 'XLC']
start = dt.datetime(2019, 7, 1)
end = dt.datetime(2021, 9, 1)
ls_key = 'Adj Close'

ETF = pdr.get_data_yahoo(ticker, start, end, interval='m')

ETF['Adj Close'].to_csv('BeautifulAnts/data/ETF/ETF_price.csv')
```



- vim SPY_price.py

```python
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

key = 'B48ELPKMWRBUJCMP'

ts = TimeSeries(key, output_format='pandas')
data, meta = ts.get_monthly_adjusted(symbol = "SPY")

data = data[data.index >= '2019-06-30']
data = data[data.index <= '2021-08-31']

data = data[['5. adjusted close']]
data.columns = ['Adj Close']

data.to_csv('BeautifulAnts/data/SPY/SPY_price.csv')
```



```python
# terminal
# terminal

pip3 install pandas
pip3 install matplotlib

# excel을 읽어들이기 위한 라이브러리 설치
pip3 install openpyxl
pip3 install xlrd

# openAPI key를 활용해 data를 읽어오기 위한 라이브러리 설치
pip3 install pandas_datareader
pip3 alpha_vantage
pip3 install quandl


hdfs dfs -mkdir -p /user/ubuntu/data

hdfs dfs -put data/dict /user/ubuntu/data/dict
hdfs dfs -put data/Article_List_excel /user/ubuntu/data/Article_List_excel


# Article_List_csv 는 python3 change_file_format.py 실행 후 시도
hdfs dfs -put BeautifulAnts/data/Article_List_csv /user/ubuntu/data/Article_List_csv

# Industrial > monthly / daily
hdfs dfs -put BeautifulAnts/data/Industrial /user/ubuntu/data/Industrial
hdfs dfs -put BeautifulAnts/data/score  /user/ubuntu/data/score

# ETF > ETF_price.csv / ETF_monthly > 각각의 *_monthly.csv
hdfs dfs -put BeautifulAnts/data/ETF  /user/ubuntu/data/ETF


# SPY > SPY_price.csv / SPY_monthly > 각각의 *_monthly.csv
hdfs dfs -put BeautifulAnts/data/SPY  /user/ubuntu/data/SPY

```



- pyspark

```python
from pyspark.sql.functions import *
from pyspark.sql.window import *
```

- pyspark - Industrial 3개월

```python
path = '/home/ubuntu/BeautifulAnts/data/Industrial'
file_list = os.listdir(path)
file_list_csv = [file for file in file_list if file.endswith('.csv')] 
file_list_csv 

for file in file_list_csv:
    company = file.split('.')[0]
    globals()['{}'.format(company)] = spark.read.format('csv').option('header','true').load('BeautifulAnts/data/Industrial/{}'.format(file))
    
    globals()['{}'.format(company)].createOrReplaceTempView('{}'.format(company))
    
    globals()['nnext_{}_month'.format(company)] = spark.sql("SELECT Date AS new_date, {} AS after_3month FROM {}".format(company,company))
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].filter('index >=2')
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].select('index','new_Date','after_3month')
    
    
    globals()['{}'.format(company)] = globals()['{}'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['{}'.format(company)] = globals()['{}'.format(company)].filter('index <= 24')
    globals()['{}'.format(company)] = globals()['{}'.format(company)].select('index', 'Date','{}'.format(company))
    globals()['{}_merge'.format(company)] = globals()['{}'.format(company)].join(globals()['nnext_{}_month'.format(company)], globals()['{}'.format(company)].index == globals()['nnext_{}_month'.format(company)].index,'outer').select('Date','{}'.format(company),'after_3month').sort('Date')
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumn('yield', ( col('after_3month') - col('{}'.format(company)) ) / col('{}'.format(company)) )
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumn('Ticker',lit('{}'.format(company)))
    globals()['{}_merge'.format(company)].createOrReplaceTempView('{}_merge'.format(company))
    
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].select(date_add(col('Date'),4),'Ticker','{}'.format(company),'after_3month','yield')
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumnRenamed('date_add(Date, 4)', 'Date2')
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumn("Date2", f.trunc("Date2", "month"))
    
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumn("Type",lit('Industry'))
    globals()['{}_merge'.format(company)].createOrReplaceTempView('{}_merge'.format(company))
    globals()['{}_merge'.format(company)] = spark.sql("SELECT Date2 AS Date, Ticker, {} AS Price, after_3month AS After_3month, yield AS Yield, Type FROM {}_merge".format(company,company))
    globals()['{}_merge'.format(company)].write.jdbc('jdbc:mysql://localhost:3306/BeautifulAnts','Derivatives_month','append',properties={'driver':'com.mysql.cj.jdbc.Driver','user':'root','password':'1234'})
```



- pyspark - ETF 3개월

```python
ETF = spark.read.format('csv').option('header','true').load('BeautifulAnts/data/ETF/ETF_price.csv')
ETF.createOrReplaceTempView('ETF')
ticker = ['IYK', 'IXN', 'IBUY', 'PBS', 'PJP', 'SOXX', 'RTH', 'MJ', 'FTXG', 'XLC']
for company in ticker :  
    globals()['{}'.format(company)] = spark.sql("SELECT add_months(Date,1) as Date, {} FROM ETF".format(company))
    
    globals()['{}'.format(company)].createOrReplaceTempView('{}'.format(company))
    
    globals()['{}_3month'.format(company)] = spark.sql("SELECT {} FROM {} WHERE Date > '2019-10-01'".format(company, company))
    globals()['{}_3month'.format(company)].createOrReplaceTempView('{}_3month'.format(company))
    globals()['nnext_{}_month'.format(company)] = spark.sql("SELECT Date AS new_Date, {} AS after_3month FROM {}".format(company,company))
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].filter('index >=2')
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].select('index','new_Date','after_3month')
    globals()['{}'.format(company)] = globals()['{}'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['{}'.format(company)] = globals()['{}'.format(company)].filter('index <= 24')
    globals()['{}'.format(company)] = globals()['{}'.format(company)].select('index', 'Date','{}'.format(company))
    
    globals()['{}_merge'.format(company)] = globals()['{}'.format(company)].join(globals()['nnext_{}_month'.format(company)], globals()['{}'.format(company)].index == globals()['nnext_{}_month'.format(company)].index,'outer').select('Date','{}'.format(company),'after_3month').sort('Date')
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumn('yield', ( col('after_3month') - col('{}'.format(company)) ) / col('{}'.format(company)) )
    
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumn('Ticker',lit('{}'.format(company)))
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumn("Type",lit('ETF'))
    globals()['{}_merge'.format(company)].createOrReplaceTempView('{}_merge'.format(company))
    globals()['{}_merge'.format(company)] = spark.sql("SELECT Date,Ticker,{} AS Price, after_3month AS After_3month, yield AS Yield, Type FROM {}_merge".format(company,company))
    
    globals()['{}_merge'.format(company)].write.jdbc('jdbc:mysql://localhost:3306/BeautifulAnts','Derivatives_month','append',properties={'driver':'com.mysql.cj.jdbc.Driver','user':'root','password':'1234'})
```

- pyspark - SPY 3개월

```python
SPY = spark.read.format('csv').option('header','true').load('BeautifulAnts/data/SPY/SPY_price.csv')
SPY.createOrReplaceTempView('SPY')
SPY = SPY.withColumnRenamed('Adj Close', 'AdjClose')
SPY = SPY.select('date', 'AdjClose').sort('date', desc=False)

nnext_month = SPY.withColumnRenamed('AdjClose','after_3month').withColumnRenamed('date','new_Date')
nnext_month = nnext_month.withColumn('index',monotonically_increasing_id())

window = Window.orderBy(col('index'))
nnext_month = nnext_month.withColumn('index', row_number().over(window))
nnext_month = nnext_month.filter("index >= 3")
nnext_month = nnext_month.withColumn('index', row_number().over(window))
nnext_month = nnext_month.select('index','new_Date','after_3month')

SPY = SPY.withColumn('index',monotonically_increasing_id())
SPY = SPY.withColumn('index', row_number().over(window))
SPY = SPY.filter('index <= 24')
SPY = SPY.select('index', 'date', 'AdjClose')

SPY_merge = SPY.join(nnext_month, SPY.index == nnext_month.index, 'outer').select('date', 'AdjClose', 'after_3month').sort('date')

SPY_merge = SPY_merge.withColumn('yield',(SPY_merge.after_3month - SPY_merge.AdjClose) / SPY_merge.AdjClose)
SPY_merge = SPY_merge.withColumn('index',monotonically_increasing_id())
window = Window.orderBy(col('index'))
SPY_merge = SPY_merge.withColumn('index', row_number().over(window))

import pyspark.sql.functions as f

SPY_d = SPY_merge.select(date_add(col('date'),4))
SPY_d = SPY_d.withColumnRenamed('date_add(date, 4)', 'Date2')
SPY_d = SPY_d.withColumn("Date2", f.trunc("Date2", "month"))

SPY_d = SPY_d.withColumn('index',monotonically_increasing_id())
window = Window.orderBy(col('index'))
SPY_d = SPY_d.withColumn('index', row_number().over(window))

SPY_final = SPY_merge.join(SPY_d, SPY_merge.index == SPY_d.index, 'outer').select('Date2', 'AdjClose', 'after_3month', 'yield').sort('date2')
SPY_final = SPY_final.withColumnRenamed('Date2', 'Date')
SPY_final = SPY_final.withColumnRenamed('AdjClose', 'Price')

SPY_final = SPY_final.withColumn('Ticker',lit('SPY'))
SPY_final = SPY_final.withColumn('Type',lit('SPY'))
SPY_final = SPY_final.select('Date','Ticker','Price','after_3month','yield','Type')

SPY_final.write.jdbc('jdbc:mysql://localhost:3306/BeautifulAnts','Derivatives_month','append',properties={'driver':'com.mysql.cj.jdbc.Driver','user':'root','password':'1234'})

```
