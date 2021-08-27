import tensorflow.compat.v1 as tf

# 1. 데이터 준비
# 2. 데이터 분할
train_X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

train_y = [
    [0],
    [1],
    [1],
    [0]
]

X = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# 3. 준비

# 가설
W = tf.Variable(tf.random_normal([2, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

logits = tf.matmul(X, W) + b
H = tf.sigmoid(logits)


# loss
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=y))


# optimizer(Gradient Descent)
learning_rate = 0.1
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

# Session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 4. 학습
epochs = 30000
for step in range(epochs) :
    _, loss_val = sess.run([train, loss], feed_dict={X: train_X, y: train_y})
    if step % 500 == 0:
        print("loss : ", loss_val)

#5. 예측 및 평가
predict = tf.cast(H > 0.5, dtype=tf.float32)
correct = tf.equal(predict, y)
accuracy = tf.reduce_mean(tf.cast(correct, dtype=tf.float32))


print("accuracy : ", sess.run(accuracy, feed_dict={X: train_X, y: train_y}))
