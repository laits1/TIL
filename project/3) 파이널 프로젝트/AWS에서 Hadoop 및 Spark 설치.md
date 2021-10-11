# AWS에서 Hadoop 및 Spark 설치



ip : 35.76.178.23

id : ubuntu



---

## Hadoop 설치

1. 업데이트

```sh
sudo apt update -y
sudo apt upgrade -y
sudo apt install vim -y
sudo apt install openssh-server ssh-askpass -y
```

2.  ssh 생성

```sh
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

3. java 설치

```sh
wget https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz

tar xvzf amazon-corretto-11-x64-linux-jdk.tar.gz
mv amazon-corretto-11.0.12.7.1-linux-x64 java
```

4. hadoop 설치

```sh
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz

tar xvzf hadoop-3.3.1.tar.gz
mv hadoop-3.3.1 hadoop
```

5. Path 설정

```sh
sudo vim ~/.bashrc 맨밑에

# JAVA
export JAVA_HOME=/home/lab09/java
export PATH=$PATH:$JAVA_HOME/bin

# hadoop
export HADOOP_HOME=/home/lab09/hadoop
export HADOOP_CONF_DIR=/home/lab09/hadoop/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# hadoop user
export HDFS_NAMENODE_USER=lab09
export HDFS_DATANODE_USER=lab09
export HDFS_SECONDARYNAMENODE_USER=lab09
export YARN_RESOUCEMANAGER_USER=lab09
export YARN_NODEMANAGER_USER=lab09


source ~/.bashrc
java -version
javac -version



cd $HADOOP_CONF_DIR
vim hadoop-env.sh
54 번째 줄
export JAVA_HOME=/home/lab09/java
58 번째 줄
export HADOOP_HOME=/home/lab09/hadoop
68 번째 줄
export HADOOP_CONF_DIR=/home/lab09/hadoop/etc/hadoop

vim core-site.xml
<property>
		<name>fs.defaultFS</name>
		<value>hdfs://localhost:9000</value>
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

5. 하둡 실행

```sh
cd

hdfs namenode -format
hdfs datanode -format
start-dfs.sh 
start-yarn.sh
jps # 6개나옴
496 ResourceManager
32150 NameNode
32343 DataNode
32649 SecondaryNameNode
698 NodeManager
1103 Jps

hdfs dfsadmin -report # Live datanodes(1) 뜬다.

# JPS가 제대로 다 안뜨면 stop-all.sh 하고 cd /tmp
# rm -rf hadoop* 하고 hdfs 포멧부터 다시

```



6. spark 설치

```sh
sudo apt install python3-pip -y
pip install numpy

wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-without-hadoop.tgz

tar xvzf spark-3.1.2-bin-without-hadoop.tgz
mv spark-3.1.2-bin-without-hadoop spark

vim ~/.bashrc 
# PATH 설정
export SPARK_HOME=/home/lab09/spark
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin
export SPARK_DIST_CLASSPATH=$(${HADOOP_HOME}/bin/hadoop classpath)

설정 후
source ~/.bashrc

cd spark/conf
cp spark-env.sh.template spark-env.sh

vim spark-env.sh
맨 밑에
export JAVA_HOME=/home/lab09/java
export HADOOP_CONF_DIR=/home/lab09/hadoop/etc/hadoop
export YARN_CONF_DIR=/home/lab09/hadoop/etc/hadoop
export SPARK_DIST_CLASSPATH=$(/home/lab09/hadoop/bin/hadoop classpath)

cp workers.template workers
cp spark-defaults.conf.template spark-defaults.conf

vim spark-defaults.conf
맨밑에
spark.master		yarn
```

