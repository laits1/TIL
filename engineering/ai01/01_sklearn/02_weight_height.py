# pip install pandas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 공공데이터포털 -> 교육부 학생건강검사 결과 분석 rawdata 서울 2015

# 몸무게를 입력하면, 키를 예측하고 싶다..

# 데이터 준비
pd.set_option("display.width", 300)
pd.set_option("display.max_rows", 1000)
pd.set_option("display.max_columns", 30)
df = pd.read_csv("weight_height.csv", encoding="euc-kr")
# print(df)

df = df[["학교명", "학년", "성별", "키", "몸무게"]]
df.dropna(inplace=True)
# print(df)

#
# 학년 값 : 1 2 3 4 5 6 1 2 3 1 2 3 -> 1 2 3 4 5 6 7 8 9 10 11 12
# hint : 초등학교 0 중학교 6 고등학교 9
# grade = [1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 3]

df['grade'] = list(map(lambda x: 0 if x[-4:] == "초등학교"
else (6 if x[-3:] == "중학교" else 9), df["학교명"])) + df["학년"]
#
# print(df)
df.drop(["학교명", "학년"], axis="columns", inplace=True)
df.columns = ["gender", "height", "weight", "grade"]
# print(df)

df["gender"] = df["gender"].map(lambda x: 0 if x == "남" else 1)
# df["gender"] = df["gender"].map({"남":0, "여":1 })

# print(df["gender"])

is_boy = df["gender"] == 0
boy_df, girl_df = df[is_boy], df[~is_boy]

# print(girl_df)

X = boy_df["weight"]
y = boy_df["height"]


# train / test set 분리

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)

train_X = train_X.values.reshape(-1, 1)
test_X = test_X.values.reshape(-1, 1)

# 모델 준비
linear = LinearRegression()

# 학습

linear.fit(train_X, train_y)

# 예측 및 평가

predict = linear.predict(test_X)
# print(test_X)
# print(predict)
# print(test_y)

# 그래프로 보자
plt.plot(test_X, test_y, "b.")
plt.plot(test_X, predict, "r.")

plt.xlim(10, 140)
plt.ylim(100, 220)
plt.grid()
# plt.show()

# 몸무게 : 80 키는?
pred_grd = linear.predict([[50]])
print("남학생 키 예측 : ", pred_grd)
