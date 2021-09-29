# ETF 전처리 스파크 코드





## 파일불러오기

```python
hdfs dfs -put ETF.csv ETF.csv

from pyspark.sql.types import StructType, StructField, StringType
schema = StructType([ StructField("Date", StringType(), True), 
                     StructField("IYK", StringType(), True), 
                     StructField("IXN", StringType(), True),
                     StructField("IBUY", StringType(), True),
                     StructField("PBS", StringType(), True),
                     StructField("PJP", StringType(), True),
                     StructField("SOXX", StringType(), True),
                     StructField("RTH", StringType(), True),
                     StructField("MJ", StringType(), True),
                     StructField("FTXG", StringType(), True),
                     StructField("XLC", StringType(), True),
                     
                    ]) 

ETF = spark.read.format('csv').option('header','true').load('ETF.csv')


# df생성
ETF.createOrReplaceTempView('ETF')



```



## IYK

```python
#Date에 +1월씩
spark.sql("SELECT add_months(Date, 1), IYK FROM ETF").show(ETF.count())

IYK = spark.sql("SELECT add_months(Date, 1) as Date, IYK FROM ETF")
IYK.createOrReplaceTempView('IYK')
IYK_3month = spark.sql("SELECT IYK FROM IYK WHERE Date > '2019-10-01'")
IYK_3month.createOrReplaceTempView('IYK_3month')

from pyspark.sql.functions import *
# 3달 후 주가 df 생성
nnext_month = spark.sql('SELECT Date AS new_date, IYK AS after_3month FROM IYK')
nnext_month = nnext_month.withColumn('index',monotonically_increasing_id())

nnext_month = nnext_month.filter("index >= 3")
nnext_month = nnext_month.withColumn('index',monotonically_increasing_id())
nnext_month = nnext_month.select('index','new_Date','after_3month')

# amd df와 nnext_month df의 열 개수 맞추기
IYK = IYK.withColumn('index',monotonically_increasing_id())
IYK = IYK.filter('index <= 22')
IYK = IYK.select('index', 'Date','IYK')

# df 병합

IYK_merge = IYK.join(nnext_month, IYK.index == nnext_month.index, 'outer').select('Date','IYK','after_3month').sort('Date')

# 수익률 column 계산해서 추가
IYK_merge = IYK_merge.withColumn('yield',(IYK_merge.after_3month - IYK_merge.IYK) / IYK_merge.IYK)
```

```py

```

## IXN

```python
#Date에 +1월씩
spark.sql("SELECT add_months(Date, 1), IXN FROM ETF").show(ETF.count())

IXN = spark.sql("SELECT add_months(Date, 1) as Date, IXN FROM ETF")
IXN.createOrReplaceTempView('IXN')
IXN_3month = spark.sql("SELECT IXN FROM IXN WHERE Date > '2019-10-01'")
IXN_3month.createOrReplaceTempView('IXN_3month')

from pyspark.sql.functions import *
# 3달 후 주가 df 생성
nnext_month = spark.sql('SELECT Date AS new_date, IXN AS after_3month FROM IXN')
nnext_month = nnext_month.withColumn('index',monotonically_increasing_id())

nnext_month = nnext_month.filter("index >= 3")
nnext_month = nnext_month.withColumn('index',monotonically_increasing_id())
nnext_month = nnext_month.select('index','new_Date','after_3month')

# amd df와 nnext_month df의 열 개수 맞추기
IXN = IXN.withColumn('index',monotonically_increasing_id())
IXN = IXN.filter('index <= 22')
IXN = IXN.select('index', 'Date','IXN')

# df 병합

IXN_merge = IXN.join(nnext_month, IXN.index == nnext_month.index, 'outer').select('Date','IXN','after_3month').sort('Date')

# 수익률 column 계산해서 추가
IXN_merge = IXN_merge.withColumn('yield',(IXN_merge.after_3month - IXN_merge.IXN) / IXN_merge.IXN)
```



## for문으로 한번에



```python
ticker = ['IYK', 'IXN', 'IBUY', 'PBS', 'PJP', 'SOXX', 'RTH', 'MJ', 'FTXG', 'XLC']
from pyspark.sql.functions import *
IYK = spark.sql("SELECT add_months(Date, 1) as Date, IYK FROM ETF")
IXN = spark.sql("SELECT add_months(Date, 1) as Date, IXN FROM ETF")
IBUY = spark.sql("SELECT add_months(Date, 1) as Date, IBUY FROM ETF")
PBS = spark.sql("SELECT add_months(Date, 1) as Date, PBS FROM ETF")
PJP = spark.sql("SELECT add_months(Date, 1) as Date, PJP FROM ETF")
SOXX = spark.sql("SELECT add_months(Date, 1) as Date, SOXX FROM ETF")
RTH = spark.sql("SELECT add_months(Date, 1) as Date, RTH FROM ETF")
MJ = spark.sql("SELECT add_months(Date, 1) as Date, MJ FROM ETF")
FTXG = spark.sql("SELECT add_months(Date, 1) as Date, FTXG FROM ETF")
XLC = spark.sql("SELECT add_months(Date, 1) as Date, XLC FROM ETF")


for company in ticker :
    globals()['{}'.format(company)].createOrReplaceTempView(company)
    globals()['{}_3month'.format(company)] = spark.sql("SELECT {} FROM {} WHERE Date > '2019-10-01'".format(company, company))
    globals()['{}_3month'.format(company)].createOrReplaceTempView('{}_3month'.format(company))
    
    # 3달 후 주가 df 생성
    globals()['nnext_{}_month'.format(company)] = spark.sql("SELECT Date AS new_date, {} AS after_3month FROM {}".format(company,company))
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].filter('index >=3')
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['nnext_{}_month'.format(company)] = globals()['nnext_{}_month'.format(company)].select('index','new_Date','after_3month')
    
    
    # amd df와 nnext_month df의 열 개수 맞추기 
    globals()['{}'.format(company)] = globals()['{}'.format(company)].withColumn('index',monotonically_increasing_id())
    globals()['{}'.format(company)] = globals()['{}'.format(company)].filter('index <= 22')
    globals()['{}'.format(company)] = globals()['{}'.format(company)].select('index', 'Date','{}'.format(company))
    
	# df 병합
    globals()['{}_merge'.format(company)] = globals()['{}'.format(company)].join(globals()['nnext_{}_month'.format(company)], globals()['{}'.format(company)].index == globals()['nnext_{}_month'.format(company)].index,'outer').select('Date','{}'.format(company),'after_3month').sort('Date')
	# 수익률 column 계산해서 추가
    globals()['{}_merge'.format(company)] = globals()['{}_merge'.format(company)].withColumn('yield', ( col('after_3month') - col('{}'.format(company)) ) / col('{}'.format(company)) )

```

```python
#DB에 저장 ticker = ['IYK', 'IXN', 'IBUY', 'PBS', 'PJP', 'SOXX', 'RTH', 'MJ', 'FTXG', 'XLC']




--
sudo mysql -u root -p
1234
show databases;
use mysql;

CREATE TABLE IYK(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);

CREATE TABLE IXN(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);
CREATE TABLE IBUY(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);
CREATE TABLE PBS(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);
CREATE TABLE PJP(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);
CREATE TABLE SOXX(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);
CREATE TABLE RTH(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);
CREATE TABLE MJ(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);
CREATE TABLE FTXG(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);
CREATE TABLE XLC(
	Date DATE,
	Price FLOAT(10,5),
	After_3month FLOAT(10,5),
	Yield FLOAT(10,5)
);

--



for company in ticker :
    user='root'
    password='1234'
    url='jdbc:mysql://localhost:3306/mysql'
    driver='com.mysql.cj.jdbc.Driver'
    dbtable = '{}'.format(company)
    globals()['{}_df'.format(company)] = spark.read.format('jdbc').option('user',user).option('password',password).option('url',url).option('driver',driver).option('dbtable',dbtable).load() 
    
    globals()['insert_{}_df'.format(company)] = globals()['{}_merge'.format(company)].toDF('Date','Price','After_3month','Yield')
    globals()['insert_{}_df'.format(company)].write.jdbc(url,dbtable,'append',properties={'driver':driver,'user':user,'password':password})
```

