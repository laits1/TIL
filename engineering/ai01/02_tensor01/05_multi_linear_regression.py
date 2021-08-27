import tensorflow.compat.v1 as tf

# 1. 데이터 준비
# 2. 데이터 분할
# 쪽지시험 3번 점수/ 실제 평가 결과

train_X =[
    [73, 80, 75],
    [93, 88, 93],
    [89, 91, 90],
    [96, 89, 100],
    [73, 66, 70]
]

train_y = [
    [80],
    [91],
    [88],
    [94],
    [61]
]

# 형태 : 변수의 종류(쪽지시험 3번)는 변하지 않는다
X = tf.placeholder(shape=[None, 3], dtype=tf.float32)
y = tf.placeholder(shape=[None, 1], dtype=tf.float32)


# 3. 준비
# 가설
W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

H = tf.matmul(X, W) + b

# loss function
loss = tf.reduce_mean(tf.square(H - y))

# optimizer
# gradient descent (경사 하강법)
laerning_rate = 0.00004
optimizer = tf.train.GradientDescentOptimizer(laerning_rate)
train = optimizer.minimize(loss)


# Session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 4. 학습
epochs = 10000000
for step in range(epochs) :
    _, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={X: train_X, y: train_y})
    if step % 1000 == 0:
        print("W: {} \t b: {} \t loss: {}".format(W_val, b_val, loss_val))

# 5. 예측 및 평가
print(sess.run(H, feed_dict={X: [[100, 80, 87]]}))