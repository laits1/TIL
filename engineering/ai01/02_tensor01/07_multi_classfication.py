import tensorflow.compat.v1 as tf

# 1. 데이터 준비
# 2. 데이터 분할
# 쪽지 시험 4번(10점 만점) / 상 : 0 중: 1 하 : 2
train_X = [
    [10, 7, 8, 5],
    [8, 8, 9, 4],
    [7, 8, 2, 3],
    [6, 3, 9, 3],
    [7, 5, 7, 4],
    [3, 5, 6, 2],
    [2, 4, 3, 1]
]
train_y = [
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 1]
]

X = tf.placeholder(shape=[None, 4], dtype=tf.float32)
y = tf.placeholder(shape=[None, 3], dtype=tf.float32)
# 3. 준비
# 가설
W = tf.Variable(tf.random_normal([4, 3]), name='weight')
b = tf.Variable(tf.random_normal([3]), name='bias')

logits = tf.matmul(X, W) + b
H = tf.nn.softmax(logits)

# loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y))

# optimizer
learning_rate = 0.01
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

# Session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 4. 학습
epochs = 3000
for step in range(epochs):
    _, loss_val = sess.run([train, loss], feed_dict={X: train_X, y: train_y})
    if step % 300 == 0 :
        print("loss : {}".format(loss_val))


# 5. 예측 및 평가
print("예측 : ", sess.run(H, feed_dict={X: [[9, 4, 5, 1]]}))

predict = tf.argmax(H, 1)
correct = tf.equal(predict, tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct, dtype=tf.float32))
print("정확도 : ", sess.run(accuracy, feed_dict={X: train_X, y: train_y}))
