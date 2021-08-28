# 머신러닝 파이선 예제



##  1. LinearRegression() - 선형회귀

1. 선형회귀를 사용하기 위해 싸이킷런 라이브러리 호출

```python
from sklearn.linear_model import LinearRegression
```

2. ``LinearRegression`` 모델을 생성하고 그 안에 X, y 데이터를 fit 시킨다.

```python
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
X = X.reshape(-1, 1)

linear = LinearRegression()
linear.fit(X, y)

```

3. 기울기와 절편을 알고 싶다면 ``linear.coef_`` , ``linear.intercept_``
4. 예측하려면 ``predict(예상할 array)`` ,  ``linear.predict([[예상할 값]])``

```python
test_X = np.array([6, 7, 8, 9, 10])
predict = linear.predict(test_X.reshape(-1, 1))

print(predict) # [12, 14, 16, 18, 20]
```



---



##  2. train_test_split()

1. **train_test_split()** 함수를 사용하기 ``sklearn.model_selction``  호출

```python
from sklearn.model_selection import train_test_split
```

2. train_test_split 예제

```python
from sklearn.datasets import load_iris # 샘플 데이터 로딩
from sklearn.model_selection import train_test_split

data_C = np.array(range(0,100))
data_F = c_to_f(data_C)

# 데이터 준비
dataset = load_iris()

X = data_C
y = data_F

# 데이터 분할
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)

```

- 옵션 값 설명
  - **test_size** : 테스트 셋 구성의 비율을 나타냅니다. train_size의 옵션과 반대 관계에 있는 옵션 값이며, 주로 test_size를 지정. 0.3은 전체 데이터 셋의 30%를 test(validation) 셋으로 지정하겠다는 의미. **default 값은 0.25** 
  - **random_state** : 세트를 섞을 때 해당 int 값을 보고 섞으며, 하이퍼 파라미터를 튜닝시 이 값을 고정해두고 튜닝해야 매번 데이터 셋이 변경 되는 것을 방지
  - **shuffle** : ``default=True`` 입니다. split을 해주기 이전에 섞을건지 여부. 보통은 default
  - **stratify** :``defalut=None`` 입니다. classification을 다룰 때 매우 중요한 옵션 값. stratify 값을 target을 지정해주면 각각의 **class 비율(ratio)을 train / validation에 유지**해줍니다. (한 쪽에 쏠려서 분배되는 것을 방지) 만약 이 옵션을 지정해 주지 않고 classification 문제를 다룬다면, 성능의 차이가 많이 날 수 있다.
- ``train_X``에는 ``X`` 의 훈련할 데이터, ``train_y``에는 ``y``의 훈련 결과 데이터
- ``test_X`` 에는 훈련 데이터를 뺸 나머지 테스트할 데이터, ``test_y`` 에는 훈련 결과 데이터를 뺀 나머지 테스트할 결과 데이터



3. 회귀분석 시작

```python
# 회귀 분석을 위해 reshape
train_X = train_X.reshape(-1, 1)
test_X = test_X.reshape(-1, 1)

# 모델 준비
linear = LinearRegression()

# 학습
linear.fit(train.X, test_X)

# 예측 및 평가
predcit = linear.predict(test_X)

# 테스트
pred_grd = linear.predict([[40]])
print("화씨 온도 : ", pred_grd) # 104

# 정확성
accuracy = linear.score(test_X, test_y)
print("accuracy : ", accuracy) # 1.0
```





---





##  3. LogisticRegression() - 로지스틱 회귀

1. **LogisticRegression()** 함수를 사용하기 ``sklearn.model_selction``  호출

```python
from sklearn.linear_model import LogisticRegression
```

2. LogisticRegression() 예제

```python

# 1. 데이터 준비
# 공부, 과외 -> 합격/ 불합격
# [1, 0] / [0] fail
# [8, 1] / [1] pass
# a 시간 공부하고, b 시간 과외받은 학생은?
X = [
    [1, 0],
    [2, 0],
    [5, 1],
    [2, 3],
    [3, 3],
    [8, 1],
    [10, 0]
]

y = [
    [0],
    [0],
    [0],
    [0],
    [1],
    [1],
    [1]
]

# 2. 데이터 분할
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)

# 3. 모델 준비
logistic = LogisticRegression()

# 4. 학습
logistic.fit(train_X, np.ravel(train_y))


# 5. 예측 및 평가
pred = logistic.predict(test_X)

```









---

##  4. KNN

1. 

```python
from sklearn.linear_model import LogisticRegression
```

2. KNN 예제

```python
```









---

##  5. SVM

1. 

```python
from sklearn.linear_model import LogisticRegression
```

2. SVM예제

```python

```





---

##  6. DecisionTree

1. 

```python
from sklearn.linear_model import LogisticRegression
```

2.  예제

```python

```





---

##  7. RandomForest

1. 

```python
from sklearn.linear_model import LogisticRegression
```

2.  예제

```python

```





---

##  8. Kmeans

1. 

```python
from sklearn.linear_model import LogisticRegression
```

2.  예제

```python

```





##  9. tensor

1. 

```python
from sklearn.linear_model import LogisticRegression
```

2.  예제

```python

```







---

##  LinearRegression()

- 설명

| [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)([data, index, columns, dtype, copy]) | Two-dimensional, size-mutable, potentially heterogeneous tabular data. |
| ------------------------------------------------------------ | :----------------------------------------------------------: |
| 필요 import                                                  |                                                              |
| **Parameters**                                               |                         ** i***int*                          |
| **Returns**                                                  |                                                              |
|                                                              |                                                              |



---

##  LinearRegression()

- 설명

| [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)([data, index, columns, dtype, copy]) | Two-dimensional, size-mutable, potentially heterogeneous tabular data. |
| ------------------------------------------------------------ | :----------------------------------------------------------: |
| 필요 import                                                  |                                                              |
| **Parameters**                                               |                         ** i***int*                          |
| **Returns**                                                  |                                                              |
|                                                              |                                                              |



---

##  LinearRegression()

- 설명

| [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)([data, index, columns, dtype, copy]) | Two-dimensional, size-mutable, potentially heterogeneous tabular data. |
| ------------------------------------------------------------ | :----------------------------------------------------------: |
| 필요 import                                                  |                                                              |
| **Parameters**                                               |                         ** i***int*                          |
| **Returns**                                                  |                                                              |
|                                                              |                                                              |

