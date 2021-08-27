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
# 입력층
W1 = tf.Variable(tf.random_normal([2, 10]), name='weight1')
b1 = tf.Variable(tf.random_normal([10], name='bias1'))
layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)

# 히든층
W2 = tf.Variable(tf.random_normal([10,20]), name='weight2')
b2 = tf.Variable(tf.random_normal([20]), name='bias2')
layer2 = tf.sigmoid(tf.matmul(layer1, W2) + b2)

# 히든층
W3 = tf.Variable(tf.random_normal([20, 10]), name='weight3')
b3 = tf.Variable(tf.random_normal([10]), name='bias3')
layer3 = tf.sigmoid(tf.matmul(layer2, W3) + b3)


# 출력층
W4 = tf.Variable(tf.random_normal([10, 1]))
b4 = tf.Variable(tf.random_normal([1], name='bias4'))
logits = tf.matmul(layer3, W4) + b4

H = tf.sigmoid(logits)
# loss
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=y))
# optimizer
learning_rate = 0.1
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

# Session
sess = tf.Session()
sess.run(tf.global_variables_initializer())


# 4. 학습
epochs = 10000
for step in range(epochs):
    _, loss_val = sess.run([train, loss], feed_dict={X: train_X, y: train_y})
    if step % 1000 == 0 :
        print("loss : ", loss_val)


# 5. 예측 및 평가
print("예측 : ", sess.run(H, feed_dict={X: train_X}))

predict = tf.cast(H > 0.5 , dtype=tf.float32)
correct = tf.equal(predict, y)
accuracy = tf.reduce_mean(tf.cast(correct, dtype=tf.float32))

print("accuracy : ", sess.run(accuracy, feed_dict={X: train_X, y: train_y}))