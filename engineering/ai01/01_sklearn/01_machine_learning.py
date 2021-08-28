from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


# pip install sklearn
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# print(X)
X = X.reshape(-1, 1)
print(X)

linear = LinearRegression()

linear.fit(X, y)

test_X = np.array([6, 7, 8, 9, 10])
predict = linear.predict(test_X.reshape(-1, 1))

print(predict)
print(linear.predict([[23]]))
plt.plot(test_X, predict)
plt.show()