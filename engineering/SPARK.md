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

