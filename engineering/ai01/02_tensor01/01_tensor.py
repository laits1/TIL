# import tensorflow as tf
import tensorflow.compat.v1 as tf
# print(tf.__version__)

'''
Tensorflow
- tensor : 데이터 저장 객체
- variable : Wight, bias
- Operation : H = W * X + b(수식/노드) => 그래프
- Session : 실행환경(학습)
'''

# 상수노드
node = tf.constant(100)

# Session : 그래프 실행 (runner)
sess = tf.Session()

# 노드(그래프) 실행
print(sess.run(node))

