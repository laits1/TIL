# hadoop wordcount

```terminal
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

