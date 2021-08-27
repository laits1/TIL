import tensorflow.compat.v1 as tf

# 1. 데이터 준비
# 2. 데이터 분할
X = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)


# 3. 준비
# 가설 설정
# H = Weight * X + bias
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
H = W * X + b

# loss function (cost function)
loss = tf.reduce_mean(tf.square(H - y))

# optimizer
# 경사 하강법 (Gradient Descent) : loss function 이 최소가 되도록
# learning_rate :
optimizer = tf.train.GradientDescentOptimizer()
train = optimizer.minimize(loss)

# Session
sess = tf.Session()
# 변수 초기화
sess.run(tf.global_variables_initailizer())

# 4. 학습
# 학습 횟수 : epochs
epochs = 5000
for step in range(epochs) :
    tmp, loss_val, W_val, b_val = sess.run([train, loss, W, b], feed_dict={X:[1, 2, 3, 4], y:[3, 5, 7, 9]})
    if step % 500 == 0 :
        print("W: {} \t b: {} \t loss : {}".format(W_val,  b_val, loss_val))


# 5. 예측 및 평가
print(sess.run(H, feed_dict={X: [10, 11, 12, 13]}))