## Spark

```terminal
sudo apt update -y
sudo apt upgrade -y yh7un
sudo apt install vim -y
sudo apt install openssh-server ssh-askpass -y

### 굳이 안해도됨
sudo vim /etc/hostname
ubuntu -> engineer로 변경

sudo vim /etc/hosts
ubuntu -> engineer로 변경

reboot
###

### ssh 생성
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# java 설치
wget https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz

tar xvzf amazon-corretto-11-x64-linux-jdk.tar.gz
mv amazon-corretto-11.0.12.7.1-linux-x64 java

# hadoop 설치
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz

tar xvzf hadoop-3.3.1.tar.gz
mv hadoop-3.3.1 hadoop

sudo vim ~/.bashrc 맨밑에
# JAVA
export JAVA_HOME=/home/engineer/java
export PATH=$PATH:$JAVA_HOME/bin

# hadoop
export HADOOP_HOME=/home/engineer/hadoop
export HADOOP_CONF_DIR=/home/engineer/hadoop/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# hadoop user
export HDFS_NAMENODE_USER=engineer
export HDFS_DATANODE_USER=engineer
export HDFS_SECONDARYNAMENODE_USER=engineer
export YARN_RESOUCEMANAGER_USER=engineer
export YARN_NODEMANAGER_USER=engineer

source ~/.bashrc
java -version
javac -version




```



```terminal
cd $HADOOP_CONF_DIR
vim hadoop-env.sh
54 번째 줄
export JAVA_HOME=/home/engineer/java
58 번째 줄
export HADOOP_HOME=/home/engineer/hadoop
68 번째 줄
export HADOOP_CONF_DIR=/home/engineer/hadoop/etc/hadoop

vim core-site.xml
<property>
		<name>fs.defaultFS</name>
		<value>hdfs://engineer:9000</value>
	</property>



vim hdfs-site.xml
	<property>
		<name>dfs.replication</name>
		<value>1</value>
	</property>
	

vim mapred-site.xml
	<property>
		<name>mapreduce.framework.name</name>
		<value>yarn</value>
	</property>
```



```shell
cd

hdfs namenode -format
hdfs datanode -format
start-dfs.sh 
start-yarn.sh
jps # 6개나옴
hdfs dfsadmin -report # Live datanodes(1) 뜬다.

# stop-all.sh  sh 전부끄기

firefox 켜서 localhost:9870

# sh 끄기
stop-dfs.sh
stop-yarn.sh
```



```SHELL
sudo apt install python3-pip -y
pip install numpy

# spark
google에 spark donwload

release : 3.1.2(JUN 01 2021)
package type : Pre-built with user-provided Apache Hadoop
Download Saprk 링크 클릭

wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-without-hadoop.tgz

tar xvzf spark-3.1.2-bin-without-hadoop.tgz
mv spark-3.1.2-bin-without-hadoop spark

# PATH 설정
sudo vim ~/.bashrc

export SPARK_HOME=/home/engineer/spark
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin
export SPARK_DIST_CLASSPATH=$(${HADOOP_HOME}/bin/hadoop classpath)

설정 후
source ~/.bashrc

cd spark/conf
cp spark-env.sh.template spark-env.sh

vim spark-env.sh
맨 밑에
export JAVA_HOME=/home/engineer/java
export HADOOP_CONF_DIR=/home/engineer/hadoop/etc/hadoop
export YARN_CONF_DIR=/home/engineer/hadoop/etc/hadoop
export SPARK_DIST_CLASSPATH=$(/home/engineer/hadoop/bin/hadoop classpath)


cp workers.template workers
cp spark-defaults.conf.template spark-defaults.conf

vim spark-defaults.conf
맨밑에
spark.master		yarn
```

```shell
cd

pyspark
ctrl + d

start-all.sh
jps
pyspark

ctrl L
```



```shell
pyspark 
# rdd
rdd01 = sc.range(0, 1000, 1, 2)
# 파티션 개수 확인
rdd01.getNumPartitions()
# 출력
rdd01.collect()
rdd01.take(5)
# 홀수만
rdd02 = rdd01.filter(lambda x:x%2)
# 짝수만
rdd03 = rdd01.filter(lambda x: not x %2)
```



```shell
countries =["korea", "united states america", "united kingdom", "japan", "germany", "france", "canada", "italy", "korea"]

g8 = sc.parallelize(countries, 2)
g8.count()
g8.collect()

# transformation
g8 = g8.distinct()
g8.count()
g8.collect()

g8_upper = g8.map(lambda x:x.upper())
g8_upper.collect()
# map : 각각의 요소에
g8_list01 = g8.map(lambda x:list(x))
g8_list01.collect()
# flatMap : 전체 요소에
g8_list02 = g8.flatMap(lambda x:list(x))
g8_list02.collect()

counting = sc.range(1, 9, 1, 2)
counting_g8 = counting.zip(g8)
counting_g8.collect()

score = [("kang", 10),("you", 30), ("kang", 20), ("shin", 60), ("youn",100)]

score_rdd = sc.parallelize(score, 2)
score_rdd_sum = score_rdd.reduceByKey(lambda x,y:x+y)
score_rdd_sum.collect()

nums = sc.parallelize([1, 3, 2, 1, 5, 4, 6, 7], 2)
nums.sortBy(lambda x: x).collect()

arr = g8.glom()
arr.collect()

# action

g8.first()
nums.max()
nums.min()

nums.mean()
nums.variance()
nums.stdev()

# stats: count mean stdev max min
nums.stats()

g8.take(3)
g8.takeOrdered(3)
g8.top(3)

nums.count()
nums.countByValue()
# countApprox(제한시간 ms, 신뢰도)
nums.countApprox(400, 0.9)

rdd02.sum()

rdd02.reduce(lambda x, y: x+y)
# fold(기본값, 연산)
rdd02.fold(0, lambda x, y: x+y)

rdd02.glom().collect()

rdd02.aggregate(0, max, lambda x, y: x + y)


# g8 에서 가장 긴 단어 찾기
def g8Max(x, y):
	if len(x) > len(y):
		return x
	else :
	return y

g8.reduce(g8Max)

# g8 가장 짧은 단어
g8.reduce(lambda x, y:y if len(x) > len(y) else x)



g8.saveAsTextFile("/tmp/g8")
# 새 터미널에서
hdfs dfs -ls /tmp/g8 # 이나
standalone : ls /tmp/g8


result = sc.textFile("/tmp/g8/part-*")
result.collect()

# key:value
key = g8.keyBy(lambda x:x[0])
key.collect()

key.mapValues(lambda x:list(x)).collect()
key.flatMapValues(lambda x: list(x)).collect()

key.groupByKey().mapValues(lambda x:list(x)).collect()

# reduceByKey 사용해서
# [('g', 'germany'), ... , ('u', 'united stats america')]
```





```python
import sys, re
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Word Count")
sc = SparkContext(conf=conf)

if (len(sys.argv) != 3):
    print("wordcount.py input_file output_dir 형태로 실행해주세요!")
    sys.exit(0)
else:
    inputpath = sys.argv[1]
    outputpath = sys.argv[2]

wordcount = sc.textFile(inputpath)\
			  .repartition(10)\
    		  .filter(lambda x: len(x) > 0)\
        	  .flatMap(lambda x: re.split("\W+", x))\
              .filter(lambda x: len(x) > 0)\
              .map(lambda x: (x.lower(), 1))\
              .reduceByKey(lambda x, y: x + y)\
              .map(lambda x: (x[1], x[0]))\
              .sortByKey(ascending=False)\
              .persist()
 
wordcount.saveAsTextFile(outputpath)
top10 = wordcount.take(10)
result = []
for counts in top10:
    result.append(counts[1])
print(result)

```

# AWS

scp -i 경로/키 경로/data.zip 계정@ip:/home/계정/



scp -i  C:\key\key\de-c2.pem C:\\data.zip lab10@3.34.168.105:/home/lab10

8910

mkdir result

spark-submit wordcount.py ./data/shakespeare.txt result



---

```shell 
mkdir data

unzip data.zip -d ./data

cd

vim wordcount.py 
# 위에 복사

# hadoop
cd data
hdfs dfs -put shakespeare.txt shakespeare.txt

cd
spark-submit wordcount.py shakespeare.txt result

# 안되면
hdfs dfs -rm -r result
하고 다시

# hadoop
hdfs dfs -cat result/part-*
```



# hadoop wordcount

```terminal
cd $HADOOP_CONF_DIR
# HADOOP_CONF_DIR = hadoop/etc/hadoop
# mapred-site.xml

<property>
	<name>yarn.app.mapreduce.am.env</name>
	<value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
</property>
<property>
	<name>mapreduce.map.env</name>
	<value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
</property>
<property>
	<name>mapreduce.reduce.env</name>
	<value>HADOOP_MAPRED_HOME=$HADOOP_HOME</value>
</property>

# yarn-site.xml
<property>
	<name>yarn.nodemanager.aux-services</name>
	<value>mapreduce_shuffle</value>
</property>

# 실행방법
cd data
hdfs dfs -put shakespeare.txt shakespeare.txt

cd
hadoop jar hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar wordcount shakespeare.txt /output
hdfs dfs -cat /output/part-r-*
	
```

---



0907 SPARK



```sh
myRange = spark.range(1000).toDF("number")
divisBy2 = myRange.where("number % 2 = 0")
divisBy2.head(10)
divisBy2.count

새 터미널
hdfs dfs -put data data
#spark
flights2010 = spark.read.csv("data/flights/csv/2010-summary.csv")
flights2010.printSchema()
flights2010.take(5)

#
flights2010 = spark.read.option("header","true").csv("data/flights/csv/2010-summary.csv")
flights2010.printSchema()
flights2010.take(5)

# 실행 계획
flights2010.sort("count").explain()

# shuffle partition 변경
spark.conf.set("spark.sql.shuffle.partitions", "5")
flights2010.sort("count").take(2)

f2015 = spark.read.format("json").load("data/flights/json/2015-summary.json")
f2015.show()
f2015.show(f2015.count())

# table 만들기
f2015.createOrReplaceTempView("flights2015")

f2015.groupBy("DEST_COUNTRY_NAME").count().show()

# spark.sql
spark.sql("SELECT DEST_COUNTRY_NAME, COUNT(1) FROM flights2015 GROUP BY DEST_COUNTRY_NAME").show()

spark.sql("SELECT DEST_COUNTRY_NAME, SUM(COUNT) FROM flights2015 GROUP BY DEST_COUNTRY_NAME").show()

spark.sql("SELECT MAX(count) FROM flights2015").show()

from pyspark.sql.functions import max
f2015.select(max("count")).show()

f2015.select("DEST_COUNTRY_NAME").show(5)
spark.sql("SELECT DEST_COUNTRY_NAME FROM flights2015 limit 5").show()

from pyspark.sql.functions import col
f2015.select(col("DEST_COUNTRY_NAME")).show(5)

from pyspark.sql.functions import expr
f2015.select(expr("DEST_COUNTRY_NAME AS destination")).show(5)
f2015.select(col("DEST_COUNTRY_NAME").alias("destination")).show(5)
f2015.select(expr("DEST_COUNTRY_NAME").alias("destination")).show(5)
spark.sql("SELECT DEST_COUNTRY_NAME as destination FROM flights2015").show(5)

# selectExpr = select + expr
f2015.selectExpr("DEST_COUNTRY_NAME as destination").show(5)
f2015.selectExpr("*","(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as DOMESTIC_FLIGHT").show()
spark.sql("SELECT *, (DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as DOMESTIC_FLIGHT FROM flights2015").show()

f2015.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show()
spark.sql("SELECT AVG(count), COUNT(DISTINCT(DEST_COUNTRY_NAME)) FROM flights2015").show()

# lit = literal (값)
from pyspark.sql.functions import lit
f2015.select(expr("*"), lit(1).alias("one")).show(1)
spark.sql("SELECT *, 1 as one FROM flights2015").show(1)


# withColumn("컬럼명", "표현식")
f2015.withColumn("DOMESTIC_FLIGHT", expr("DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME")).show()
spark.sql("SELECT *, (DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) AS DOMESTIC_FLIGHT FROM flights2015").show()


# withColumnRenamed
f2015.withColumnRenamed("DEST_COUNTRY_NAME", "DESTINATION").show()
f2015.columns

f2015.filter(col("count") <2).show(5)
f2015.where("count < 2").show(5)
spark.sql("SELECT * FROM flights2015 WHERE count < 2").show(5)
spark.sql("SELECT * FROM flights2015 WHERE count < 2 AND ORIGIN_COUNTRY_NAME !='Croatia'").show()
f2015.where("count < 2").where(col("ORIGIN_COUNTRY_NAME") != "Croatia").show(5)

spark.sql("SELECT COUNT(DISTINCT(ORIGIN_COUNTRY_NAME, DEST_COUNTRY_NAME)) AS count FROM flights2015").show(5)
f2015.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()

from pyspark.sql import Row
schema = f2015.schema
new_rows = [
	Row("Korea", "Korea", 5),
	Row("Korea", "Austrailia", 1)
]

paralle_rows = sc.parallelize(new_rows)
new_df = spark.createDataFrame(paralle_rows, schema)

f2015.union(new_df).show(10000)

f2015.orderBy(col("count").asc()).show(f2015.count())
f2015.sort("count").show(f2015.count())
spark.sql("SELECT * FROM flights2015 ORDER BY count ASC").show(f2015.count())
f2015.orderBy(col("count").desc()).show(f2015.count())

# DEST_COUNTRY_NAME 을 기준으로 오름차순으로 정렬하고, COUNT를 기준으로 오름차순으로 정렬
f2015.orderBy(col("DEST_COUNTRY_NAME"), col("count")).show(f2015.count())
f2015.sort("DEST_COUNTRY_NAME","count").show(f2015.count())

spark.sql("SELECT * FROM flights2015 ORDER BY DEST_COUNTRY_NAME, count").show(f2015.count())

# DEST_COUNTRY_NJAME 을 내림차순, count는 오름차순으로 정렬해서 출력
spark.sql("SELECT * FROM flights2015 ORDER BY DEST_COUNTRY_NAME DESC, count").show(f2015.count())
f2015.orderBy(col("DEST_COUNTRY_NAME").desc(), expr("count asc")).show(5)
from pyspark.sql.functions import desc
f2015.sort(desc("DEST_COUNTRY_NAME"), col("count")).show(5)
f2015.sort(f2015.DEST_COUNTRY_NAME.desc(), col("count").asc()).show(5)

# limit
f2015.limit(5).show()
spark.sql("SELECT * FROM flights2015 LIMIT 5").show()
```





6문제 만들기

```sql
# f2015 에서 DEST_COUNTRY_NAME을 그룹화 하고 DEST_COUNT_NAME과 각 COUNT를 더한 컬럼을 출력

spark.sql("SELECT DEST_COUNTRY_NAME, SUM(COUNT) FROM flights2015 GROUP BY DEST_COUNTRY_NAME").show()


# f2015에서 DEST_COUNTRY_NAME을 그룹화 하고 DEST_COUNTRY_NAME이 United로 시작하는 컬럼 출력
spark.sql("SELECT DEST_COUNTRY_NAME FROM flights2015 WHERE DEST_COUNTRY_NAME LIKE 'United%' GROUP BY DEST_COUNTRY_NAME").show()

# f2015에서 DEST_COUNTRY_NAME과 ORIGIN_COUNTRY_NAME이 같은 모든 컬럼을 출력
spark.sql("SELECT * FROM flights2015 WHERE DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME").show()

# F2015에서 count가 200보다 크고 300보다 작으면서 DEST_COUNTRY_NJAME 을 내림차순
spark.sql("SELECT * FROM flights2015 WHERE COUNT > 200 AND COUNT < 300 ORDER BY DEST_COUNTRY_NAME DESC").show()

# F2015에서 count가 1000보다 작으면서 COUNT를 내림차순
spark.sql("SELECT * FROM flights2015 WHERE COUNT > 1000 ORDER BY COUNT DESC").show()

# count가 1이면서 DEST_COUNTRY_NAME이 United States가 아닌 모든 컬럼 출력
spark.sql("SELECT * FROM flights2015 WHERE COUNT = 1 AND DEST_COUNTRY_NAME != 'United States' ORDER BY DEST_COUNTRY_NAME DESC").show()
```



```sh
# **Q. f2015 테이블에 가고싶은 여행지를 3곳이상 등록하세요.** (출발지는 한국, count는 같이가고싶은 사람수)

new_rows = [
	Row("Korea", "Japan", 20000),
	Row("Korea", "China", 3), 
	Row("Korea", "Canada", 4)
]
paralle_rows = sc.parallelize(new_rows)
new_df = spark.createDataFrame(paralle_rows, schema)

f2015.union(new_df).show(10000)


# **Q. 추가한 f2015를 count를 기준으로 내림차순 정렬하세요**
spark.sql("SELECT * FROM flights2015 ORDER BY COUNT DESC").show()

# **Q. count가 193이상인 컬럼을 count를 기준으로 오름차순 정렬하여 전체항목을 보여주세요.**
spark.sql("SELECT * FROM flights2015 where COUNT >= 193 ORDER BY COUNT ASC").show()

# **Q. 도착하는 국가의 문자열 개수가 13개미만인 국가의 이름만 출력하여 전체항목을 보여주세요.**
spark.sql("SELECT * FROM flights2015 ")

# **Q. ORIGIN_COUNTRY_NAME의 문자열 개수가 10개미만인 국가의 모든 column을 출력하세요.**

# **Q. 국내선만 출력하시오(출발지와 도착지가 같은)**

# Q1:flights2015 데이터중  count가 100~200사이인 데이터를 뽑으세요. (SQL 형식)

# Q2: flights2015의 count의 평균값을 구하시오 

# Q3: f2015 에서 count가 10000이상인 것 10개를 보여주시오

# Q4: f2015에서 ORIGIN_COUNTRY_NAME 을 departure 으로 바꿔주세요 (sql사용)

# Q5: DEST_COUNTRY_NAME 컬럼을 기준으로 내림차순으로 정렬하세요

# Q6: withcolumnrename을 이용해 DEST_COUNTRY_NAME을 arrive_to 로 바꿔주세요

# # DEST_COUNTRY_NAME을 DEST, ORIGIN_COUNTRY_NAME을 ORIGIN으로 컬럼명 표현, count를 내림차순 정렬orderBy 사용

# count가 1000이 넘는 모든 컬럼 출력 (filter사용)

# ORIGIN_COUNTRY_NAME을 ORIGIN으로 표시하고 오름차순 출력 (expr 사용)

# Q1: f2015에서 ORIGIN_COUNTRY_NAME 을 departing_from 으로 바꿔주세요 (select, expr을 사용해주세요)

# Q2: f2015에서 모든 컬럼을 출력하고 destination 과 origin 이 다른 flight 를 international_flight라는 컬럼을 만들어서 표현하시오 (SQL 방식)
 
# Q3: Renamed을 사용하여 ORIGIN_COUNTRY_NAME을 departure 로 바꾸시오

# Q4: f2015에서 모든 컬럼을 출력하고 미국에서 출발하는 컬럼을 departing_from_US 로만들어서 표현하시오 (SQL 방식)

# Q5. FLIGHTS2015에서 평균(average) count를 구하시오 (SQL 이용)

# Q6: f2015 에서 count가 1000이상인 것 5개를 보여주시오 

```







---

9/8



```shell
retails = spark.read.format("csv").option("header","true")\
.option("inferSchema", "true").load("data/retails/2010-12-01.csv")

# 우분투만 새 터미널 열어서
hdfs dfs -mkdir -p /user/engineer
hdfs dfs -put data /user/engineer


retails.printSchema()
retails.createOrReplaceTempView("retails")


from pyspark.sql.functions import lit
retails.select(lit(5), lit("five"), lit(5.0))

from pyspark.sql.functions import col
retails.where(col("InvoiceNo") != 536365).select("InvoiceNo", "Description").show(5)
retails.select("InvoiceNo", "Description").where(col("InvoiceNo") != 536365).show(5)

from pyspark.sql.functions import instr
price_filter = col("UnitPrice") > 600
descript_filter = instr(retails.Description, "POSTAGE") >= 1

dot_code_filter = col("StockCode") == "DOT"

retails.withColumn("isExpensive", dot_code_filter & (price_filter | descript_filter)).where("isExpensive").select("UnitPrice", "isExpensive").show(5)

spark.sql("SELECT UnitPrice, (StockCode= 'DOT' AND (UnitPrice > 600 OR instr(Description,'POSTAGE') >= 1)) AS isExpensive FROM retails WHERE (StockCode = 'DOT' AND (UnitPrice > 600 OR instr(Description,'POSTAGE') >= 1))").show(5)


from pyspark.sql.functions import pow
# (현재 개수 * 가격) ^2 + 5
real_quantity = pow(col("Quantity") * col("UnitPrice)"), 2) + 5

from pyspark.sql.functions import expr
retails.select(col("CustomerId"), expr("(POWER((Quantity * UnitPrice), 2) + 5) AS RealQuantity")).show(5)

retails.select(col("CustomerId"), real_quantity.alias("RealQuantity")).show(5)

from pyspark.sql.functions import round, bround
retails.select(round(lit("2.5")), bround(lit("2.5"))).show(1)
spark.sql("SELECT ROUND(2.5), BROUND(2.5)").show()

retails.describe().show()
from pyspark.sql.functions import count, mean, stddev_pop, min, max
retails.select(count("UnitPrice"), mean("UnitPrice"), stddev_pop("UnitPrice"), min("UnitPrice"), max("UnitPrice")).show()

from pyspark.sql.functions import monotonically_increasing_id
retails.select("*", monotonically_increasing_id()).show(5)

# Description의 첫글자만 대문자, 나머지는 소문자로 출력
from pyspark.sql.functions import initcap
retails.select(initcap(col("DESCRIPTION"))).show(5, False)

# DESCRIPTION 전체를 소문자로, DESCRIPTION 전체를 대문자로 한번에 출력하자.
from pyspark.sql.functions import lower, upper
retails.select(lower(col("DESCRIPTION")), upper(col("DESCRIPTION"))).show(5, False)

# spark.sql 을 dataframe 형식으로 바꾸자.
spark.sql("SELECT LTRIM('	HELLO	'), RTRIM('	HELLO	'), TRIM('	HELLO	'), LPAD('HELLO',10,'*'),RPAD('HELLO', 10, '*')").show(2)

from pyspark.sql.functions import ltrim, rtrim, trim, lpad, rpad
retails.select(ltrim(lit('	HELLO	')), rtrim(lit("	HELLO	")), trim(lit('	HELLO	')), trim(lit("HELLO")), lpad(lit("HELLO"), 10, "*"), rpad(lit("HELLO"), 10, "*")).show(1)

from pyspark.sql.functions import regexp_replace
regex_str = "BLACK|WHITE|RED|GREEN|BLUE"
retails.select(regexp_replace(col("DESCRIPTION"), regex_str, "COLOR").alias("color"), col("DESCRIPTION")).show(5, False)

spark.sql("SELECT REGEXP_REPLACE(DESCRIPTION, 'BLACK|WHITE|RED|GREEN|BLUE', 'COLOR') as color, DESCRIPTION FROM retails").show(5, False)

# 왜안댐?
spark.sql("""
SELECT REGEXP_REPLACE(DESCRIPTION, 'BLACK|WHITE|RED|GREEN|BLUE', 'COLOR') as color, DESCRIPTION FROM retails
""").show(5, False)

from pyspark.sql.functions import translate
retails.select(translate(col("DESCRIPTION"), "ABCD", "1234"), col("DESCRIPTION")).show(5, False)
#

# 패턴추출
from pyspark.sql.functions import regexp_extract
extract_str = "(BLACK|WHITE|RED|GREEN|BLUE)"
retails.select(regexp_extract(col("DESCRIPTION"), extract_str, 1).alias("extract"), col("DESCRIPTION")).show(5, False)

from pyspark.sql.functions import instr
contains_black = instr(col("DESCRIPTION"), "BLACK") >= 1
contains_white = instr(col("DESCRIPTION"), "WHITE") >= 1
retails.withColumn("hasBlackWhite", contains_black | contains_white).select("DESCRIPTION", "hasBlackWhite").show(5, False)

# DESCRIPTION 컬럼에서 BLACK 이나 WHITE 라는 단어를 포함한 ROW만 출력
retails.withColumn("hasBlackWhite", contains_black | contains_white).where("hasBlackWhite").select(col("DESCRIPTION"), col("hasBlackWhite")).show(5, False)


# date : 달력(연:월:일)
# timestamp : 달력 + 시간(연:월:일 시:분:초)
from pyspark.sql.functions import current_date, current_timestamp
date_df = spark.range(10).withColumn("today_date", current_date()).withColumn("now_timestamp", current_timestamp())
date_df.createOrReplaceTempView("dateTable")
date_df.printSchema()
date_df.show(1, False)

from pyspark.sql.functions import date_add, date_sub
date_df.select(date_sub(col("today_date"), 5), date_add(col("today_date"), 5)).show(1)
spark.sql("SELECT date_sub(today_date, 5), date_add(today_date, 5) FROM dateTable").show(1)

from pyspark.sql.functions import datediff, months_between, to_date
# 날짜 차이
date_df.withColumn("week_ago", date_sub(col("today_date"), 7))\
.select(datediff(col("week_ago"), col("today_date"))).show(1)

# 개월수 차이
date_df.select(to_date(lit("2021-06-21")).alias("start"), to_date(lit("2021-11-12")).alias("end")).select(months_between(col("start"), col("end"))).show(1)

spark.sql("""
SELECT DATEDIFF(DATE_SUB(today_date, 7), today_date) as datediff, months_between('2021-06-21', '2021-11-12') as monthsbet FROM dateTable
""").show(1)

# null , 안나옴. 실제날짜가 아니라서.
date_df.select(to_date(lit("2021-12-32"))).show(1)

# simpleDateFormat (Java)
dateFormat = "yyyy-MM-dd"
clean_date = spark.range(1).select(to_date(lit("2021-11-12"), dateFormat).alias("date"), to_date(lit("2021-12-32"), dateFormat).alias("date2"))
clean_date.show()
#
clean_date.createOrReplaceTempView("dateTable2")
spark.sql("""
SELECT TO_DATE(date, 'yyyy-MM-dd'), TO_DATE(date, 'yyyy-dd-MM')
FROM dateTable2
""").show()
#



from pyspark.sql.functions import to_timestamp
clean_date.select(to_timestamp(col("date"), dateFormat)).show()

clean_date.select(to_date(col("date"), "yyyy-MM-dd HH:mm:ss"), \
to_timestamp(col("date"), "yyyy-MM-dd HH:mm:ss")).show()

spark.sql("""
SELECT TO_DATE('2021-11-12 17:55:00', 'yyyy-MM-dd HH:mm:ss') as date, TO_TIMESTAMP('2021-11-12 17:55:00', 'yyyy-MM-dd HH:mm:ss') as timestamp
""").show()

from pyspark.sql import Row
null_df = sc.parallelize([
	Row(name="Kang", phone="010-0000-0000", address="Seoul"),
	Row(name="Shin", phone="010-1111-1111", address=None),
	Row(name="You", phone=None, address=None)	
]).toDF()
          
null_df.createOrReplaceTempView("nullTable")

from pyspark.sql.functions import coalesce
null_df.select(coalesce(col("address"), col("phone"))).show()

# ifnull : 첫 번째 값이 null이면 , 두번째 값 리턴
# nullif : 두 값이 같으면, null 리턴
# nvl : 첫번째 값이 null이면, 두번째 값 리턴
# nvl2 : 첫번째 값이 null이 아니면 두번째 값 리턴, null이면 세번째 값 리턴
spark.sql("""
SELECT IFNULL(NULL, 'VALUE'), NULLIF('SAME', 'SAME'), NVL(NULL, 'VALUE'), NVL2(NULL, 'VALUE', 'ELSE-VALUE')
""").show()

null_df.count()
null_df.na.drop().count()
null_df.na.drop().show()

# na : null 값을 처리하기 위해 DataFrameNaFunction 리턴
# DataFrameNaFunction : drop, fill, replace
null_df.na.drop("any").count() # null값 하나라도 있으면 제외함
null_df.na.drop("all").count() # 모두 null이어야 제외함

null_df.na.drop("all", subset=["phone"]).show() # phone 값이 널이면 지움.
null_df.na.drop("all", subset=["phone", "address"]).show()
null_df.na.drop("any", subset=["phone", "address"]).show()


null_df.na.fill("n/a").show()
null_df.na.fill("n/a", subset=["name", "address"]).show()
fill_cols_val ={"phone":"070-7777-7777","address":"heaven"}
null_df.na.fill(fill_cols_val).show()

null_df.na.replace(["Seoul"], ["서울"], "address").show()

# 구조체 : dataframe 내부에 dataframe
retails.selectExpr("(DESCRIPTION, INVOICENO) AS complex", "*").show(5, False)
retails.selectExpr("struct(DESCRIPTION, INVOICENO) AS complex", "*").show(5, False)

from pyspark.sql.functions import struct
complex_df = retails.select(struct("DESCRIPTION", "INVOICENO").alias("complex"))
complex_df.createOrReplaceTempView("complexDF")
complex_df.select("complex").show(5, False)
complex_df.select("complex.DESCRIPTION").show(5, False)
complex_df.select(col("complex").getField("DESCRIPTION")).show(5, False)

complex_df.select("complex.*").show(5, False)
complex_df.select("complex").show(5, False)

```



---

9/9



```sh
# vmware만
vim start.sh

hdfs namenode -format
hdfs datanode -format

start-dfs.sh
start-yarn.sh

hdfs dfs -mkdir -p /user/engineer
hdfs dfs -put data /user/engineer/

chmod 755 start.sh
./start.sh
```



```sh
retails = spark.read.format("csv").option("header","true").load("data/retails/2010-12-01.csv")
from pyspark.sql.functions import split
from pyspark.sql.functions import col
retails.select(split(col("DESCRIPTION"), " ")).show(5, False)

retails.createOrReplaceTempView("retails")
spark.sql("SELECT SPLIT(DESCRIPTION, ' ') FROM retails").show(5, False)

from pyspark.sql.functions import size
retails.select(size(split(col("DESCRIPTION"), " ")).alias("size")).show(5)

retails.select(split(col("DESCRIPTION"), " ").alias("array_col")).selectExpr("array_col[0]").show(5)

from pyspark.sql.functions import array_contains
retails.select(array_contains(split(col("DESCRIPTION"), " "), "WHITE")).show(5)
spark.sql("SELECT ARRAY_CONTAINS(SPLIT(DESCRIPTION, ' '), 'WHITE') FROM retails").show(5)

# explode : 배열 타입의 컬럼을 입력 받아 해당 배열 값에 포함된 모든 로우로 반환.(나머지 컬럼은 중복)
from pyspark.sql.functions import explode

retails.withColumn("splitted", split(col("DESCRIPTION"), " ")).select("DESCRIPTION", "splitted").show(7, False)
retails.withColumn("splitted", split(col("DESCRIPTION"), " ")).withColumn("exploded", explode(col("splitted"))).show(7, False)

# 맵
from pyspark.sql.functions import create_map
retails.select(create_map(col("STOCKCODE"), col("DESCRIPTION")).alias("complex_map")).show(5,False)
spark.sql("SELECT MAP(STOCKCODE,DESCRIPTION) as complex_map FROM retails WHERE DESCRIPTION IS NOT NULL").show(5, False)

retails.select(create_map(col("STOCKCODE"), col("DESCRIPTION")).alias("complex_map")).selectExpr("complex_map['71053']").show()

retails.select(create_map(col("STOCKCODE"), col("DESCRIPTION")).alias("complex_map")).selectExpr("explode(complex_map)").show()


# 사용자 정의 함수
def power3(value):
	return value**3


from pyspark.sql.functions import udf
pow3 = udf(power3)

user_def_df = spark.range(5).toDF("nums")
user_def_df.select(pow3(col("nums")), col("nums")).show()

retails_all = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("data/retails/*.csv")
retails_all.createOrReplaceTempView("retailsAll")

from pyspark.sql.functions import count
retails_all.select(count("STOCKCODE")).show()
spark.sql("SELECT COUNT(STOCKCODE) FROM retailsALL").show()

from pyspark.sql.functions import countDistinct
retails_all.select(countDistinct("*").alias("countDistinct")).show()
spark.sql("SELECT COUNT(DISTINCT(*)) AS countDistinct FROM retailsAll").show()

from pyspark.sql.functions import first, last
retails_all.select(first("STOCKCODE"), last("STOCKCODE")).show()
spark.sql("SELECT FIRST(STOCKCODE), LAST(STOCKCODE) FROM retailsAll").show()

from pyspark.sql.functions import min,max
retails_all.select(min("QUANTITY"), max(
"QUANTITY")).show()
spark.sql("SELECT MIN(QUANTITY), MAX(QUANTITY) FROM retailsAll").show()

from pyspark.sql.functions import sum
retails_all.select(sum("QUANTITY")).show()
spark.sql("SELECT SUM(QUANTITY) FROM retailsAll").show()

from pyspark.sql.functions import sumDistinct
retails_all.select(sumDistinct("QUANTITY")).show()
spark.sql("SELECT SUM(DISTINCT(QUANTITY)) FROM retailsAll").show()

from pyspark.sql.functions import avg, expr
retails_all.select(count("QUANTITY").alias("countQ"), sum("QUANTITY").alias("sumQ"), avg("QUANTITY").alias("avgQ"), expr("mean(QUANTITY)").alias("meanQ")).selectExpr("sumQ / countQ", "avgQ", "meanQ").show()

# 분산, 표준편차
from pyspark.sql.functions import var_pop, stddev_pop
from pyspark.sql.functions import var_samp, stddev_samp
# var_pop(모분산) /  stddev_pop (모 표준편차)
# var_samp (표본분산) / stddev_samp (표본 표준편차)
# 모집단 : 전체, 표본집단 : 일부

retails_all.select(var_pop("QUANTITY").alias("varpop"), var_samp("QUANTITY").alias("varsamp"), stddev_pop("QUANTITY").alias("stddevpop"), stddev_samp("QUANTITY").alias("stddevsamp")).show()

# 공분산, 상관관계
# corr : 피어슨 상관관계
# covar_pop : 모집단 공분산
# covar_samp : 표본 공분산
from pyspark.sql.functions import corr, covar_pop, covar_samp
retails_all.select(corr("INVOICENO", "QUANTITY").alias("corr:"),covar_pop("INVOICENO", "QUANTITY").alias("covarpop"), covar_samp("INVOICENO", "QUANTITY").alias("covarsamp")).show(5)

# 집합 agg (aggregate)
from pyspark.sql.functions import collect_set, collect_list
# collect_set : 중복 제거 집합
# collect_list : 중복 있는 집합
retails_all.agg(collect_set("COUNTRY"), collect_list("COUNTRY")).show()
spark.sql("SELECT COLLECT_SET(COUNTRY), COLLECT_LIST(COUNTRY) FROM retailsAll").show()

retails_all.groupBy("INVOICENO", "CUSTOMERID").count().show()
spark.sql("SELECT INVOICENO, CUSTOMERID, count(*) FROM retailsAll GROUP BY INVOICENO, CUSTOMERID").show()
```





9/13

```sh
```

