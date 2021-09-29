# Daily전처리 스파크 코드





## 파일불러오기

```python
# 터미널
hdfs dfs -put ./BeautifulAnts/data/daily/daily.csv daily.csv
hdfs dfs -put ./BeautifulAnts/data/daily/SHV.csv SHV.csv
hdfs dfs -put ./BeautifulAnts/data/daily/SPY.csv SPY.csv

# 파일 불러오기
daily = spark.read.format('csv').option('header','true').load('daily.csv')
SPY = spark.read.format('csv').option('header','true').load('SPY.csv')
SHV = spark.read.format('csv').option('header','true').load('SHV.csv')

ticker = ['MSFT', 'AMD', 'AMZN', 'KO', 'MCD', 'MO', 'NKE', 'PFE', 'WMT']

from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import *
from pyspark.sql import functions
from pyspark.sql.functions import col
import pyspark.sql.functions as F
from pyspark.sql.window import Window


# 가로행을 더한 portfolio_value 컬럼 추가
expression = '+'.join(ticker)
daily = daily.withColumn('portfolio_value', expr(expression))

# Date 로 정렬
daily = daily.sort('Date')

# portfolio_value의 pct 계산한  portfolio_return 컬럼 추가

window = Window.orderBy("Date")
lagCol = lag(col("portfolio_value"), 1).over(window)
daily = daily.withColumn("new", lagCol)

daily = daily.withColumn('portfolio_return', (daily['portfolio_value']-daily['new']) / daily['new'])

daily = daily.drop(daily.new)

# lag_portfolio_return  = 모멘텀
lagCol = lag(col("portfolio_return"), 1).over(window)
daily = daily.withColumn("lag_portfolio_return", lagCol)

daily = daily.drop(daily.portfolio_return)

# SPY
daily = daily.join(SPY, on=['date'], how='left_outer')
# SHV
daily = daily.join(SHV, on=['date'], how='left_outer')

# EXMKT 컬럼
daily = daily.withColumn('EXMKT', daily['SPY'] - daily['SHV'])


# 컬럼명 변경
daily = daily.withColumnRenamed('portfolio_value','Value')
daily = daily.withColumnRenamed('lag_portfolio_return', 'Momentum') 

```



## DB 에 저장

```mysql
sudo mysql -u root -p



user='root'
password='1234'
url='jdbc:mysql://localhost:3306/BeautifulAnts'
driver='com.mysql.cj.jdbc.Driver'
dbtable = 'daily'

daily.write.jdbc(url,dbtable,'append',properties={'driver':driver,'user':user,'password':password})


```







​    
