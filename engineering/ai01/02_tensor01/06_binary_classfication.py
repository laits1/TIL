import tensorflow.compat.v1 as tf

# logistic regression

# 1. 데이터 준비
# 2. 데이터 분할
# [1, 0] : 1시간 공부 / 0시간 과외 -> [0] : fail
# [8, 1] : 8시간 공부 / 1시간 과외 -> [1] : pass
train_X = [
    [1, 0],
    [2, 0],
    [5, 1],
    [2, 3],
    [3, 3],
    [8, 1],
    [10, 0]
]

train_y = [
    [0],
    [0],
    [0],
    [0],
    [1],
    [1],
    [1],
]
X = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# 3. 준비
# 가설
W = tf.Variable(tf.random_normal([2, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

logit = tf.matmul(X, W) + b
# actvation function : sigmoid 사용 (0 또는 1)

H = tf.sigmoid(logit)

# loss
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit, labels=y))


# optimizer(Gradient Descent)
learning_rate = 0.1
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)



# Session
sess = tf.Session()
sess.run(tf.global_variables_initializer())


# 4. 학습
epochs = 10000
for step in range(epochs) :
    _, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={X: train_X, y: train_y})
    if step % 500 == 0:
        print("W : {}\t b : {} \t loss : {}".format(W_val, b_val, loss_val))

#5. 예측 및 평가
predict = tf.cast(H > 0.5, dtype=tf.float32)

equal = tf.cast(tf.equal(predict, y), dtype=tf.float32)
accuracy = tf.reduce_mean(equal)

# 우리는 지금 데이터의 볼륨이 작아서 학습데이터를 넣어줬지만,
# 사실 test_set()이 필요!

print(sess.run(accuracy, feed_dict={X: train_X, y: train_y}))

print("예측 : ", sess.run(H, feed_dict={X: [[4, 2]]}))

