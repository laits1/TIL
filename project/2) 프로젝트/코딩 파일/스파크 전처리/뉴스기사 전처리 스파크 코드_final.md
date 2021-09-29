# 기사점수파일 전처리 스파크 코드





## 파일불러오기

```python
# 터미널
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/ALTRIA_scda.csv ALTRIA.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/Amazon_scda.csv Amazon.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/AMD_scda.csv AMD.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/Coca-cola_scda.csv Cocacola.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/Facebook_scda.csv Facebook.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/Microsoft_scda.csv Microsoft.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/NIKE_scda.csv NIKE.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/PFIZER_scda.csv PFIZER.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/Spotify_scda.csv Spotify.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/TESLA_scda.csv TESLA.csv
hdfs dfs -put ./BeautifulAnts/data/Article_score_csv/Walmart_scda.csv Walmart.csv


# pyspark
ticker = ['ALTRIA','Amazon','AMD','Cocacola','Facebook','Microsoft', 'NIKE', 'PFIZER', 'Spotify', 'TESLA', 'Walmart']
from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import *

# 날짜 형식
    
before_months = ["Jul-19", "Aug-19", "Sep-19","Oct-19","Nov-19","Dec-19",
                 "Jan-20","Feb-20","Mar-20","Apr-20","May-20","Jun-20","Jul-20", "Aug-20", "Sep-20","Oct-20","Nov-20","Dec-20",
                 "Jan-21","Feb-21","Mar-21","Apr-21","May-21","Jun-21","Jul-21", "Aug-21", "Sep-21"]
after_months = ["2019-07", "2019-08","2019-09","2019-10","2019-11","2019-12",
                "2020-01","2020-02","2020-03","2020-04","2020-05","2020-06","2020-07","2020-08","2020-09","2020-10","2020-11","2020-12",
                "2021-01","2021-02","2021-03","2021-04","2021-05","2021-06","2021-07","2021-08","2021-09"]  

for company in ticker :
    # 파일 불러오기
    globals()['{}_at'.format(company)] = spark.read.format('csv').option('header','true').load('{}.csv'.format(company))
    # 점수 계산해서 컬럼추가
    globals()['{}_at'.format(company)] =globals()['{}_at'.format(company)].withColumn('sent',(globals()['{}_at'.format(company)].npos - globals()['{}_at'.format(company)].nneg) / globals()['{}_at'.format(company)].nwords)
    # 점수 계산 NULL값 0으로 변경
    globals()['{}_at'.format(company)] = globals()['{}_at'.format(company)].fillna(0)
    # _co, nwords, npos, nneg 컬럼 제거
    globals()['{}_at'.format(company)] = globals()['{}_at'.format(company)].drop('nwords', 'npos', 'nneg')
    
    # 날짜 슬라이싱
    globals()['{}_at'.format(company)] = globals()['{}_at'.format(company)].withColumn("date", substring(col("date"), 4,6))
    
    # 날짜 형식 변경
    globals()['{}_at'.format(company)] = globals()['{}_at'.format(company)].na.replace(before_months, after_months, 'date')
    
    # groupby
    globals()['{}_at'.format(company)] = globals()['{}_at'.format(company)].groupBy("date").mean("sent").sort("date")
    
    # 컬럼명 변경
    globals()['{}_at'.format(company)] = globals()['{}_at'.format(company)].withColumnRenamed('avg(sent)', 'sent')
    
    #globals()['{}_at'.format(company)].show(globals()['{}_at'.format(company)].count())
	
```

