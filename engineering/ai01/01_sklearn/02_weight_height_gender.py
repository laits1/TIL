import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



# 1. 데이터 준비
df = pd.read_csv("weight_height.csv", encoding="euc-kr")
df = df[["학교명", "학년", "성별", "키", "몸무게"]]
df.dropna(inplace=True)

df["grade"] = list(map(lambda x: 0 if x[-4:] == "초등학교" else (6 if x[-3:] == "중학교" else 9), df["학교명"])) + df["학년"]
df.drop(["학교명", "학년"], axis="columns", inplace=True)

df.columns = ['gender', 'height', 'weight', 'grade']

df['gender'] = df['gender'].map(lambda x:0 if x =='남' else 1)
# print(df)

x = df[['weight', 'gender']]
y = df['height']


# 2. 데이터 분할
train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=1)

train_y = train_y.values.reshape(-1)
test_y = test_y.values.reshape(-1)


# 3. 모델 준비
linear = LinearRegression()

# 4. 학습
linear.fit(train_X, train_y)


# 5. 예측 및 평가

predict = linear.predict(test_X)
pred_grd = linear.predict([[60, 1]])

print("키 예측 : ", pred_grd)


# 몸무게, 성별 -> 키
