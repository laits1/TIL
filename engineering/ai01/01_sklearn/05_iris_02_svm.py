from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# 1. 데이터 준비
iris = load_iris()
X = iris.data
y = iris.target

# 2. 데이터 분할
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)


# 3. 모델 준비
svm = SVC(kernel="linear")

# 4. 학습
svm.fit(train_X, train_y)

# 5. 예측 및 평가
pred = svm.predict(test_X)
for i in range(len(test_X)):
    print(test_X[i], "예측 : ", iris.target_names[pred[i]], "\t 실제 : ", iris.target_names[test_y[i]])

print(svm.score(test_X, test_y))
