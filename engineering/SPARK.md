## Spark

```terminal
sudo apt update -y
sudo apt upgrade -y 
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







