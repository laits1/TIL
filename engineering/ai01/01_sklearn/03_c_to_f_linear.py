import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def c_to_f(x) :
    return x * 1.8 + 32

data_C = np.array(range(0,100))
data_F = c_to_f(data_C)

print(type(data_C))
# 데이터 준비
x = data_C
y = data_F

# 데이터 분할
train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=1)
#
train_X = train_X.reshape(-1, 1)
test_X = test_X.reshape(-1, 1)

# 모델 준비
linear = LinearRegression()

# 학습
linear.fit(train_X, train_y)

# 예측 및 평가

predict = linear.predict(test_X)

# 테스트
pred_grd = linear.predict([[40]])
print("화씨온도 : ", pred_grd)

# 그래프로 보기
plt.plot(test_X, test_y, "b.")
plt.plot(test_X, predict, "r.")
plt.xlim(10,140)
plt.ylim(100,220)
plt.grid()
plt.show()

accuracy = linear.score(test_X, test_y)
print("accuracy : ", accuracy)