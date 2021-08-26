# pip install pandas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 공공데이터포털 -> 교육부 학생건강검사 결과 분석 rawdata 서울 2015

# 여학생의 몸무게를 입력하면, 키를 예측하고 싶다..

# 데이터 준비
pd.set_option("display.width", 300)
pd.set_option("display.max_rows", 1000)
pd.set_option("display.max_columns", 30)
df = pd.read_csv("weight_height.csv", encoding="euc-kr")

# 필요한 컬럼만 불러오기
df = df[["학교명", "학년", "성별", "키", "몸무게"]]
# print(df)

# 학년 값 변경하기하고 grade 컬럼 새롭게 만들기
# 학년 값 : 1 2 3 4 5 6 1 2 3 1 2 3 -> 1 2 3 4 5 6 7 8 9 10 11 12
df['grade'] = list(map(lambda x : 0 if x[-4:] == "초등학교"
                       else (6 if x[-3:] == "중학교" else 9), df["학교명"])) + df["학년"]
# print(df)

# "학교명"과 "학년" 컬럼 삭제 후 남은 컬럼 영어로 변경
df.drop(["학교명", "학년"], axis="columns", inplace=True)
df.columns = ["gender", "height", "weight", "grade"]
# print(df)

# gender에서 남자면 0 여자면 1로 변경
df["gender"] = df["gender"].map(lambda x: 0 if x =="남" else 1)
# print(df)

# 데이터 분할  남성 / 여성
is_boy = df["gender"] == 0
boy_df, girl_df = df[is_boy], df[~is_boy]
# print(girl_df)

# 여성 weight / height 분리

x = girl_df["weight"]
y = girl_df["height"]
print(type(x))


# train / test set 분리
train_X, test_X, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=1)

train_X = train_X.values.reshape(-1, 1)
test_X = test_X.values.reshape(-1, 1)


# 모델 준비
linear = LinearRegression()

# 학습
linear.fit(train_X, train_y)

# 예측 및 평가
predict = linear.predict(test_X)

# 그래프로 보기
plt.plot(test_X, test_y, "b.")
plt.plot(test_X, predict, "r.")
plt.xlim(10,140)
plt.ylim(100,220)
plt.grid()
plt.show()
# 테스트
# 몸무게 : 50 키는 ?
pred_grd = linear.predict([[110]])
print("여학생 키 예측 : ", pred_grd)