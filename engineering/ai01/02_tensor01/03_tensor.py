import tensorflow.compat.v1 as tf

# placeholder : 그래프를 실행하는 시점에서 데이터를 입력받아서 실행

node1 = tf.placeholder(dtype=tf.float32)
node2 = tf.placeholder(dtype=tf.float32)

node3 = node1 + node2

sess = tf.Session()

print(sess.run(node3, feed_dict={node1:[10, 20 ,30],
                                 node2:[40, 50, 60]}))
