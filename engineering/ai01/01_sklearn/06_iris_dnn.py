from sklearn.neural_network import MLPRegressor
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

# 1. 데이터 준비
iris = load_iris()
X = iris.data
y = iris.target

# 2. 데이터 분할
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)


# 3. 모델 준비
mlp = MLPRegressor(hidden_layer_sizes=(200,), activation='logistic', random_state=1)

# 4. 학습
mlp.fit(train_X, train_y)


# 5. 예측 및 평가
predict = mlp.predict(test_X)
print(predict)

accuracy = mlp.score(test_X, test_y)
print(accuracy)