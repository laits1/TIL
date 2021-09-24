

```python
# 파일 불러오기
hdfs dfs -put ETF.csv ETF.csv

ETF = spark.read.format('csv').option('header','true').load('ETF.csv')

ETF.show()

ETF = spark.read

# df생성
 ETF.createOrReplaceTempView('ETF')

# Date가 NONE인 행 삭제
dropna_altria = altria.filter(altria.new_date != 'NONE')
dropna_altria.show()

spark.sql("SELECT * FROM ETF").show()


# Date를 기준으로 월별 score 평균
dropna_altria.groupBy(substring('new_date',1,7)).agg(avg('score')).show()




```

kd

```python
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

# spark = SparkSession 
# 스키마 지정 안함 spark.read.csv("/user/shs/sample.csv").show() 
# 스키마 지정하고 읽음 spark.read.csv("/user/shs/sample.csv", header=False, schema=schema).show()
ETF.select(ETF.Date, ETF.IYK).show(ETF.count())

# df생성
ETF.createOrReplaceTempView('ETF')

#Date에 +1월씩
spark.sql("SELECT add_months(Date, 1), IYK FROM ETF").show(ETF.count())

IYK = spark.sql("SELECT add_months(Date, 1) as Date, IYK FROM ETF")
IYK.createOrReplaceTempView('IYK')
IYK_3month = spark.sql("SELECT IYK FROM IYK WHERE Date > '2019-10-01'")
IYK_3month.createOrReplaceTempView('IYK_3month')


# IYK.withColumn('3months', IYK_3month.IYK).show()


from pyspark.sql import Row


```

