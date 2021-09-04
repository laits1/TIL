import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

# 1. 데이터 준비
iris = load_iris()
X = iris.data
y = iris.target

# 2. 데이터 분할
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)


# 3. 모델 준비
mean = KMeans(n_clusters=3)  # 3개 품목 

# 4. 학습
mean.fit(train_X, train_y)


# 5. 예측 및 평가

pred = mean.predict(test_X)

df = pd.DataFrame(test_X)
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
df["category"] = pd.DataFrame(pred)

centers = pd.DataFrame(mean.cluster_centers_)
centers.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
center_X = centers["sepal_length"]
center_y = centers["sepal_width"]

plt.scatter(df["sepal_length"], df["sepal_width"], c=df["category"])
plt.scatter(center_X, center_y, s=100, c='r', marker="*")
plt.show()