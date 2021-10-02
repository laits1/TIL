# -*- coding: utf-8 -*-
"""
Created on 2021

@author: Administrator
"""

#%%

# =============================================================================
# =============================================================================
# # 문제 01 유형(DataSet_01.csv 이용)
#
# 구분자 : comma(“,”), 4,572 Rows, 5 Columns, UTF-8 인코딩
# 
# 글로벌 전자제품 제조회사에서 효과적인 마케팅 방법을 찾기
# 위해서 채널별 마케팅 예산과 매출금액과의 관계를 분석하고자
# 한다.
# 컬 럼 / 정 의  /   Type
# TV   /     TV 마케팅 예산 (억원)  /   Double
# Radio / 라디오 마케팅 예산 (억원)  /   Double
# Social_Media / 소셜미디어 마케팅 예산 (억원)  / Double
# Influencer / 인플루언서 마케팅
# (인플루언서의 영향력 크기에 따라 Mega / Macro / Micro / 
# Nano) / String

# SALES / 매출액 / Double
# =============================================================================
# =============================================================================

# 시험에서 빈번하게 사용되는 패키지
# pandas, numpy, scipy.stats, sklearn, statsmodels, matplotlib, seaborn

import pandas as pd

data1=pd.read_csv('Dataset_01.csv', na_values=['?', 'Na', ' '])
data1.info()

#%%

# =============================================================================
# 1. 데이터 세트 내에 총 결측값의 개수는 몇 개인가? (답안 예시) 23
# =============================================================================

data1.isna().sum().sum()

# 정답: 26

# (참고) 결측치가 포함된 행의 수

data1.isnull().any(axis=1).sum()

# 결측치가 포함된 행의 수: 26


#%%

# =============================================================================
# 2. TV, Radio, Social Media 등 세 가지 다른 마케팅 채널의 예산과 매출액과의 
# 상관분석을 통하여 각 채널이 매출에 어느 정도 연관이 있는지 알아보고자 한다. 
# - 매출액과 가장 강한 상관관계를 가지고 있는 채널의 상관계수를 소수점 5번째
# 자리에서 반올림하여 소수점 넷째 자리까지 기술하시오. (답안 예시) 0.1234
# =============================================================================

# 변수 선택(수치형변수)
data1.columns
# ['TV', 'Radio', 'Social_Media', 'Influencer', 'Sales']

x_var=['TV', 'Radio', 'Social_Media', 'Sales']

x_var=data1.columns.drop('Influencer')

# 강한 상관계수
q2=data1[x_var].corr().abs()
# from sklearn.linear_model import 

q2_ans=q2.drop('Sales')['Sales'].max() # 최대값
round(q2_ans,4)

# 정답:  0.999497444941335 -> 0.9995

# (참고)
q2.drop('Sales')['Sales'].max()  # 값
q2.drop('Sales')['Sales'].nlargest(1) # 인덱스, 값
q2.drop('Sales')['Sales'].idxmax()  # 인덱스
q2.drop('Sales')['Sales'].argmax() # 최대값이 있는 위치번호

#%%

# =============================================================================
# 3. 매출액을 종속변수, TV, Radio, Social Media의 예산을 독립변수로 하여 
# 회귀분석을
# 수행하였을 때, 세 개의 독립변수의 회귀계수를 큰 것에서부터 작은 것 순으로
# 기술하시오. 
# - 분석 시 결측치가 포함된 행은 제거한 후 진행하며, 회귀계수는 소수점 넷째 자리
# 이하는 버리고 소수점 셋째 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================

from sklearn.linear_model import LinearRegression

# !pip install scikit-learn
# !cd

# 입력변수, 종속변수 구분
x_var=['TV', 'Radio', 'Social_Media']

# 결측치 제거
q3=data1.dropna()

# 회귀분석
lm=LinearRegression(fit_intercept=True)
lm.fit(q3[x_var], q3.Sales)

dir(lm)
lm.intercept_ # 상수
lm.coef_  # 회귀계수
# [ 3.56256963, -0.00397039,  0.00496402]

q3_out=pd.DataFrame(lm.coef_)
q3_out.index=x_var
q3_out.sort_index()
q3_out.sort_values(0, ascending=False).values  # 기준이 되는 변수명

# 정답: 3.56256963, 0.00496402,-0.00397039
# => 3.562, 0.004,-0.003

#%%

# =============================================================================
# =============================================================================
# # 문제 02 유형(DataSet_02.csv 이용)
# 구분자 : comma(“,”), 200 Rows, 6 Columns, UTF-8 인코딩

# 환자의 상태와 그에 따라 처방된 약에 대한 정보를 분석하고자한다
# 
# 컬 럼 / 정 의  / Type
# Age  / 연령 / Integer
# Sex / 성별 / String
# BP / 혈압 레벨 / String
# Cholesterol / 콜레스테롤 레벨 /  String
# Na_to_K / 혈액 내 칼륨에 대비한 나트륨 비율 / Double
# Drug / Drug Type / String
# =============================================================================
# =============================================================================

import pandas as pd

data2=pd.read_csv('Dataset_02.csv')
data2.info()
data2.columns
# ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K', 'Drug']
#%%

# =============================================================================
# 1.해당 데이터에 대한 EDA를 수행하고, 여성으로 혈압이 High, Cholesterol이 Normal인
# 환자의 전체에 대비한 비율이 얼마인지 소수점 네 번째 자리에서 반올림하여 소수점 셋째
# 자리까지 기술하시오. (답안 예시) 0.123
# =============================================================================

# pd.crosstab(), Series.value_counts()

q1=pd.crosstab(index=[data2.Sex, data2.BP],
               columns=data2.Cholesterol, normalize=True)


q1.index
q1.loc[('F',   'HIGH'), 'NORMAL']

# 정답: 0.105

# (비교)
# data2.groupby(['Sex','BP'])['Cholesterol'].value_counts()/len(data2)

#%%

# =============================================================================
# 2. Age, Sex, BP, Cholesterol 및 Na_to_K 값이 Drug 타입에 영향을 미치는지 확인하기
# 위하여 아래와 같이 데이터를 변환하고 분석을 수행하시오. 
# - Age_gr 컬럼을 만들고, Age가 20 미만은 ‘10’, 20부터 30 미만은 ‘20’, 30부터 40 미만은
# ‘30’, 40부터 50 미만은 ‘40’, 50부터 60 미만은 ‘50’, 60이상은 ‘60’으로 변환하시오. 
# - Na_K_gr 컬럼을 만들고 Na_to_k 값이 10이하는 ‘Lv1’, 20이하는 ‘Lv2’, 30이하는 ‘Lv3’, 30 
# 초과는 ‘Lv4’로 변환하시오.
# - Sex, BP, Cholesterol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지 독립성 검정을
# 수행하시오.
# - 검정 수행 결과, Drug 타입과 연관성이 있는 변수는 몇 개인가? 연관성이 있는 변수
# 가운데 가장 큰 p-value를 찾아 소수점 여섯 번째 자리 이하는 버리고 소수점 다섯
# 번째 자리까지 기술하시오.
# (답안 예시) 3, 1.23456
# =============================================================================
# q2=data2 # 주소 참조 방식
q2=data2.copy() # 값 자체 복사해서 새로운 변수 생성, 복사 기능

# (1) 변수변환,  np.where
import numpy as np
# np.where(조건, 참인 경우 실행문, 거짓인 경우 실행문)

# - Age_gr 컬럼을 만들고, Age가 20 미만은 ‘10’, 20부터 30 미만은 ‘20’, 30부터 40 미만은
# ‘30’, 40부터 50 미만은 ‘40’, 50부터 60 미만은 ‘50’, 60이상은 ‘60’으로 변환하시오. 

q2['Age_gr']=np.where(q2.Age < 20, 10,
                np.where(q2.Age < 30, 20,
                   np.where(q2.Age < 40, 30,
                      np.where(q2.Age < 50, 40,
                         np.where(q2.Age < 60, 50, 60)))))

# - Na_K_gr 컬럼을 만들고 Na_to_K 값이 10이하는 ‘Lv1’, 20이하는 ‘Lv2’, 30이하는 ‘Lv3’, 30 
# 초과는 ‘Lv4’로 변환하시오.

q2['Na_K_gr']=np.where(q2.Na_to_K <= 10, 'Lv1',
                 np.where(q2.Na_to_K <= 20, 'Lv2',
                    np.where(q2.Na_to_K <= 30, 'Lv3', 'Lv4')))


# (2) 카이스퀘어 검정: 두 변수만을 이용함(범주형 변수)
# - 빈도 기반으로 검정함
# Sex, BP, Cholesterol, Age_gr, Na_K_gr이 Drug 변수와 영향이 있는지
# 독립성 검정을 수행

from scipy.stats import chi2_contingency  # 카이스퀘어 검정

temp=pd.crosstab(index=q2['Sex'],columns=q2['Drug'])
p_value=chi2_contingency(temp)[1]

# (3) 반복 처리

var_list=['Sex', 'BP', 'Cholesterol', 'Age_gr', 'Na_K_gr']

q2_out=[]
for i in var_list :
    temp=pd.crosstab(index=q2[i],columns=q2['Drug'])
    chi2=chi2_contingency(temp)[0]
    p_value=chi2_contingency(temp)[1]
    q2_out.append([i, chi2, p_value])

q2_out=pd.DataFrame(q2_out, 
                    columns=['var', 'chi2','p_value'])

q2_out

# (4) 종합평가, 연관성이 있는지 없는지 유무 파악
# 귀무가설(H0): 두변수가 독립이다.
# 대립가설(H1) : 두변수가 독립이 아니다.
# - 유의수준(a) 기준으로 p-value와 비교
# p-value < a : 귀무가설을 기각, 대립가설 채택, 독립이 아니다(관계가 존재)
# p-value >= a : 귀무가설을 기각할 수 없음, 귀무가설 채택, 독립이다

# 연관성이 있는 변수=> 귀무가설 기각하는 변수 목록
# Drug 타입과 연관성이 있는 변수는 몇 개인가? 
q2_ans=q2_out[q2_out.p_value < 0.05]
len(q2_ans)  # 4

# 연관성이 있는 변수 가운데 가장 큰 p-value를 찾아 
# 소수점 여섯 번째 자리 이하는 버리고 소수점 다섯번째 자리까지 기술하시오.
q2_ans.p_value.max()  # 0.0007010113024729462 => 0.00070

# 정답 : 4, 0.00070

#%%

# =============================================================================
# 3.Sex, BP, Cholesterol 등 세 개의 변수를 다음과 같이 변환하고 의사결정나무를 이용한
# 분석을 수행하시오.
# - Sex는 M을 0, F를 1로 변환하여 Sex_cd 변수 생성
# - BP는 LOW는 0, NORMAL은 1 그리고 HIGH는 2로 변환하여 BP_cd 변수 생성
# - Cholesterol은 NORMAL은 0, HIGH는 1로 변환하여 Ch_cd 생성
# - Age, Na_to_k, Sex_cd, BP_cd, Ch_cd를 Feature로, Drug을 Label로 하여 의사결정나무를
# 수행하고 Root Node의 split feature와 split value를 기술하시오. 
# 이 때 split value는 소수점 셋째 자리까지 반올림하여 기술하시오. (답안 예시) Age, 
# 12.345
# =============================================================================

q3=data2.copy()
q3.Sex.value_counts()

# 변수 변환(범주형변수->수치형 변수로 변환)

# - Sex는 M을 0, F를 1로 변환하여 Sex_cd 변수 생성
q3['Sex_cd']=np.where(q3.Sex == 'M', 0, 1)

# - BP는 LOW는 0, NORMAL은 1 그리고 HIGH는 2로 변환하여 BP_cd 변수 생성
q3['BP_cd']=np.where(q3.BP == 'LOW', 0,
               np.where(q3.BP == 'NORMAL', 1, 2))

# - Cholesterol은 NORMAL은 0, HIGH는 1로 변환하여 Ch_cd 생성
q3['Ch_cd']=np.where(q3.Cholesterol == 'NORMAL',0,1)

# 의사결정 나무 & 입력/출력 변수 확인
# => 분류문제

# - Age, Na_to_k, Sex_cd, BP_cd, Ch_cd를 Feature로, Drug을 Label

x_var=['Age', 'Na_to_K', 'Sex_cd', 'BP_cd', 'Ch_cd']

from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

dt=DecisionTreeClassifier().fit(q3[x_var], q3.Drug)


# 최종 결과 : root node의 변수와 분리 값 찾기

import matplotlib.pyplot as plt
plt.figure(figsize=(12,10))

plot_tree(dt,
          max_depth=2,
          feature_names=x_var,
          class_names=list(q3.Drug.unique()),
          precision=3,
          fontsize=7)

export_text(dt,
            feature_names=x_var,
            decimals=3)

# 정답: Na_to_K, 14.829

# (비고)
pred=dt.predict(q3[x_var])

from sklearn.metrics import classification_report, precision_score
print(classification_report(q3.Drug, pred))
# precision_score(q3.Drug, pred, pos_label='drugC')


#%%

# =============================================================================
# =============================================================================
# # 문제 03 유형(DataSet_03.csv 이용)
# 
# 구분자 : comma(“,”), 5,001 Rows, 8 Columns, UTF-8 인코딩
# 안경 체인을 운영하고 있는 한 회사에서 고객 사진을 바탕으로 안경의 사이즈를
# 맞춤 제작하는 비즈니스를 기획하고 있다. 우선 데이터만으로 고객의 성별을
# 파악하는 것이 가능할 지를 연구하고자 한다.
#
# 컬 럼 / 정 의 / Type
# long_hair / 머리카락 길이 (0 – 길지 않은 경우 / 1 – 긴
# 경우) / Integer
# forehead_width_cm / 이마의 폭 (cm) / Double
# forehead_height_cm / 이마의 높이 (cm) / Double
# nose_wide / 코의 넓이 (0 – 넓지 않은 경우 / 1 – 넓은 경우) / Integer
# nose_long / 코의 길이 (0 – 길지 않은 경우 / 1 – 긴 경우) / Integer
# lips_thin / 입술이 얇은지 여부 0 – 얇지 않은 경우 / 1 –
# 얇은 경우) / Integer
# distance_nose_to_lip_long / 인중의 길이(0 – 인중이 짧은 경우 / 1 – 인중이
# 긴 경우) / Integer
# gender / 성별 (Female / Male) / String
# =============================================================================
# =============================================================================

import pandas as pd

data3=pd.read_csv('Dataset_03.csv')
data3.columns
# ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 
# 'nose_wide', 'nose_long', 'lips_thin',
# 'distance_nose_to_lip_long', 'gender']

#%%

# =============================================================================
# 1.이마의 폭(forehead_width_cm)과 높이(forehead_height_cm) 사이의
# 비율(forehead_ratio)에 대해서 평균으로부터 3 표준편차 밖의 경우를 이상치로
# 정의할 때, 이상치에 해당하는 데이터는 몇 개인가? (답안 예시) 10
# =============================================================================


q1=data3.copy()
# 변수 생성
q1['forehead_ratio']=q1['forehead_width_cm'] / q1['forehead_height_cm']

# 기준 값 생성
xbar=q1['forehead_ratio'].mean()
std=q1['forehead_ratio'].std()

UB=xbar + (3*std)
LB=xbar - (3*std)

# 이상치 검출
len(q1[(q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] > UB)])

((q1['forehead_ratio'] < LB) | (q1['forehead_ratio'] > UB)).sum()

# 정답: 3
    
#%%

# =============================================================================
# 2.성별에 따라 forehead_ratio 평균에 차이가 있는지 적절한 통계 검정을 수행하시오.
# - 검정은 이분산을 가정하고 수행한다.
# - 검정통계량의 추정치는 절대값을 취한 후 소수점 셋째 자리까지 반올림하여
# 기술하시오.
# - 신뢰수준 99%에서 양측 검정을 수행하고 결과는 귀무가설 기각의 경우 Y로, 그렇지
# 않을 경우 N으로 답하시오. (답안 예시) 1.234, Y
# =============================================================================

# 평균 차이 검정: ttest, anova
# 그룹의 수가 2개 이하: ttest
# - 일표본 t검정, 이표본 t검정(독립, 대응) 
# 그룹의 수가 3개 이상: anova

from scipy.stats import ttest_1samp, ttest_ind, ttest_rel

# ttest_1samp : 일표본 t 검정
# ttest_ind : 독립 이표본 t 검정, 분산도 고려
# ttest_rel : 대응인 이표본 t 검정, 
# - 내부적으로는 단일 변수 생성해서 검정, 일표본 t 검정과 동일 결과

# 일표본 t 검정
# 귀무가설(H0) : mu == 180
# 대립가설(H1) : mu != 180
# => 표본 -> 통계량(xbar) -> 표준화(t) -> p-value


# 독립 이표본 t 검정 => 사전에 등분산 검정
# 귀무가설(H0) : muA == muB => muA - muB = 0
# 대립가설(H1) : muA != muB => muA - muB != 0


# 대응 이표본 t 검정 => 단일 변수 => 등분산 검정 불필요
# 귀무가설(H0) : muA == muB => muA - muB = 0 => D == 0
# 대립가설(H1) : muA != muB => muA - muB != 0 => D != 0
q1.gender.unique()

g_m=q1[q1.gender=='Male']['forehead_ratio']
g_f=q1[q1.gender=='Female']['forehead_ratio']

q2_out=ttest_ind(g_m, g_f, equal_var=False)
# 검정통계량의 추정치는 절대값을 취한 후 소수점 셋째 자리까지 반올림하여 기술
round(abs(q2_out.statistic),3)  # 평균을 t 표준화 결과

# 신뢰수준 99%에서 양측 검정을 수행하고 결과
q2_out.pvalue  # 평균을 t0 표준화한 다음 t0값 보다 극단적으로 큰값(작은값)
q2_out.pvalue < 0.01


# 정답: 2.999, Y(귀무가설 기각)

#%%

# =============================================================================
# 3.주어진 데이터를 사용하여 성별을 구분할 수 있는지 로지스틱 회귀분석을 적용하여
# 알아 보고자 한다. 
# - 데이터를 7대 3으로 나누어 각각 Train과 Test set로 사용한다. 이 때 seed는 123으로
# 한다.
# - 원 데이터에 있는 7개의 변수만 Feature로 사용하고 gender를 label로 사용한다.
# (forehead_ratio는 사용하지 않음)
# - 로지스틱 회귀분석 예측 함수와 Test dataset를 사용하여 예측을 수행하고 정확도를
# 평가한다. 이 때 임계값은 0.5를 사용한다. 
# - Male의 Precision 값을 소수점 둘째 자리까지 반올림하여 기술하시오. (답안 예시) 
# 0.12
# 
# 
# (참고) 
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# train_test_split 의 random_state = 123
# =============================================================================

from sklearn.model_selection import train_test_split

train, test=\
    train_test_split(data3,
                  test_size=0.3,random_state=123)

x_var=data3.columns.drop('gender')
x_var
# ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide',
#       'nose_long', 'lips_thin', 'distance_nose_to_lip_long']


from sklearn.linear_model import LogisticRegression

logit=LogisticRegression().fit(train[x_var], train.gender)

pred=logit.predict(test[x_var])
pred_pr=logit.predict_proba(test[x_var])

logit.intercept_
logit.coef_

type(pred_pr)

import numpy as np

np.where(pred_pr[:,1] >= 0.5, 'Male', 'Female')


from sklearn.metrics import classification_report, precision_score

print(classification_report(test.gender, pred))

#              precision    recall  f1-score   support

#       Female       0.97      0.96      0.96       743
#         Male       0.96      0.97      0.97       758

#     accuracy                           0.97      1501
#    macro avg       0.97      0.97      0.97      1501
# weighted avg       0.97      0.97      0.97      1501


precision_score(test.gender, pred, pos_label='Male')

# 정답: 0.9596354166666666 -> 0.96



#%%

# =============================================================================
# =============================================================================
# # 문제 04 유형(DataSet_04.csv 이용)
#
#구분자 : comma(“,”), 6,718 Rows, 4 Columns, UTF-8 인코딩

# 한국인의 식생활 변화가 건강에 미치는 영향을 분석하기에 앞서 육류
# 소비량에 대한 분석을 하려고 한다. 확보한 데이터는 세계 각국의 1인당
# 육류 소비량 데이터로 아래와 같은 내용을 담고 있다.

# 컬 럼 / 정 의 / Type
# LOCATION / 국가명 / String
# SUBJECT / 육류 종류 (BEEF / PIG / POULTRY / SHEEP) / String
# TIME / 연도 (1990 ~ 2026) / Integer
# Value / 1인당 육류 소비량 (KG) / Double
# =============================================================================
# =============================================================================

# (참고)
# #1
# import pandas as pd
# import numpy as np
# #2
# from scipy.stats import ttest_rel
# #3
# from sklearn.linear_model import LinearRegression

#%%

import pandas as pd

data4=pd.read_csv('Dataset_04.csv')

data4.info()
data4.columns # ['LOCATION', 'SUBJECT', 'TIME', 'Value']
# =============================================================================
# 1.한국인의 1인당 육류 소비량이 해가 갈수록 증가하는 것으로 보여 상관분석을 통하여
# 확인하려고 한다. 
# - 데이터 파일로부터 한국 데이터만 추출한다. 한국은 KOR로 표기되어 있다.
# - 년도별 육류 소비량 합계를 구하여 TIME과 Value간의 상관분석을 수행하고
# 상관계수를 소수점 셋째 자리에서 반올림하여 소수점 둘째 자리까지만 기술하시오. 
# (답안 예시) 0.55
# =============================================================================

data4.LOCATION.unique()

# 한국 데이터 추출
q1=data4[data4.LOCATION == 'KOR']

# 년도별 육류 소비량 합계
q1_tab=pd.pivot_table(q1, index='TIME',
                      values='Value', aggfunc='sum')

# q1_tab=q1.groupby('TIME')['Value'].sum()

q1_tab.reset_index(inplace=True)

q1_ans=q1_tab.corr()

q1_ans.loc['TIME', 'Value']

# 정답: 0.9601244896033334 -> 0.96

#%%

# =============================================================================
# 2. 한국 인근 국가 가운데 식생의 유사성이 상대적으로 높은 일본(JPN)과 비교하여,
# 연도별 소비량에 평균 차이가 있는지 분석하고자 한다.
# - 두 국가의 육류별 소비량을 연도기준으로 비교하는 대응표본 t 검정을 수행하시오.
# - 두 국가 간의 연도별 소비량 차이가 없는 것으로 판단할 수 있는 육류 종류를 모두
# 적으시오. (알파벳 순서) (답안 예시) BEEF, PIG, POULTRY, SHEEP
# =============================================================================

from scipy.stats import ttest_rel

# 한국/일본 데이터 추출
q2=data4[data4.LOCATION.isin(['KOR', 'JPN'])]

# 데이터셋 재구성(피벗테이블 활용), 단 결측치는 제거
# q2.pivot_table()

sub_list=q2.SUBJECT.unique()

q2_out=[]
for i in sub_list:
    temp=q2[q2.SUBJECT == i]
    tab=pd.pivot_table(temp, index='TIME',
                    columns='LOCATION',
                    values='Value').dropna()
    pvalue=ttest_rel(tab['JPN'], tab['KOR']).pvalue
    q2_out.append([i, pvalue])

q2_out=pd.DataFrame(q2_out, columns=['SUBJECT', 'pvalue'])

# 두 국가 간의 연도별 소비량 차이가 없는 것으로 판단할 수 있는 육류 종류
q2_out[q2_out.pvalue >= 0.05]

# 정답: POULTRY

#%%

# =============================================================================
# 3.(한국만 포함한 데이터에서) Time을 독립변수로, Value를 종속변수로 하여 육류
# 종류(SUBJECT) 별로 회귀분석을 수행하였을 때, 가장 높은 결정계수를 가진 모델의
# 학습오차 중 MAPE를 반올림하여 소수점 둘째 자리까지 기술하시오. (답안 예시) 21.12
# (MAPE : Mean Absolute Percentage Error, 평균 절대 백분율 오차)
# (MAPE = Σ ( | y - y ̂ | / y ) * 100/n ))
# 
# =============================================================================


# 한국 데이터 추출
q3=data4[data4.LOCATION == 'KOR']


# 육류 종류별로 회귀분석
# - 결정 계수 기록
# - MAPE
# - 결정계수가 가장 높은 모델의 MAPE 찾기

sub_list=q3.SUBJECT.unique()
# ['BEEF', 'PIG', 'POULTRY', 'SHEEP']

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

q3_out=[]
for i in sub_list:
    temp=q3[q3.SUBJECT == i]
    lm=LinearRegression().fit(temp[['TIME']], temp['Value'])  
    # X 는 2차원 구조로 입력 
    pred=lm.predict(temp[['TIME']])
    r2=lm.score(temp[['TIME']], temp['Value'])
    # r2=r2_score(temp['Value'], pred)
    
    # MAPE = Σ ( | y - y ̂ | / y ) * 100/n 
    mape= (abs(temp['Value'] - pred) /temp['Value']).sum() * 100 / len(temp)
    q3_out.append([i, r2, mape])


q3_out=pd.DataFrame(q3_out, columns=['subject', 'r2', 'mape'])

q3_out.loc[q3_out.r2.idxmax(),'mape']

# 정답: 5.783357902874552 -> 5.78



# (참고) 차원 변경
temp['TIME'].shape # (36,) 1차원 => (36,1) 2차원

temp['TIME'].values.reshape(-1,1).shape
temp[['TIME']].shape


# (비고) 육류 종류별 별도 모델 생성 후 모델 호출하기
# globals()
# locals()

q3_out=[]
for i in sub_list:
    temp=q3[q3.SUBJECT == i]
    globals()['lm_'+str(i)]=\
        LinearRegression().fit(temp[['TIME']], temp['Value'])

for i in sub_list:
    temp=q3[q3.SUBJECT == i]
    print(eval('lm_'+str(i)).predict(temp[['TIME']]))

#
temp=q3[q3.SUBJECT == 'BEEF']
lm_BEEF.predict(temp[['TIME']])

lm_BEEF.coef_
lm_PIG.coef_

#%%

# =============================================================================
# =============================================================================
# # 문제 05 유형(DataSet_05.csv 이용)
#
# 구분자 : comma(“,”), 8,068 Rows, 12 Columns, UTF-8 인코딩
#
# A자동차 회사는 신규 진입하는 시장에 기존 모델을 판매하기 위한 마케팅 전략을 
# 세우려고 한다. 기존 시장과 고객 특성이 유사하다는 전제 하에 기존 고객을 세분화하여
# 각 그룹의 특징을 파악하고, 이를 이용하여 신규 진입 시장의 마케팅 계획을 
# 수립하고자 한다. 다음은 기존 시장 고객에 대한 데이터이다.
#

# 컬 럼 / 정 의 / Type
# ID / 고유 식별자 / Double
# Age / 나이 / Double
# Age_gr / 나이 그룹 (10/20/30/40/50/60/70) / Double
# Gender / 성별 (여성 : 0 / 남성 : 1) / Double
# Work_Experience / 취업 연수 (0 ~ 14) / Double
# Family_Size / 가족 규모 (1 ~ 9) / Double
# Ever_Married / 결혼 여부 (Unknown : 0 / No : 1 / Yes : 2) / Double
# Graduated / 재학 중인지 여부 / Double
# Profession / 직업 (Unknown : 0 / Artist ~ Marketing 등 9개) / Double
# Spending_Score / 소비 점수 (Average : 0 / High : 1 / Low : 2) / Double
# Var_1 / 내용이 알려지지 않은 고객 분류 코드 (0 ~ 7) / Double
# Segmentation / 고객 세분화 결과 (A ~ D) / String
# =============================================================================
# =============================================================================


#(참고)
#1
# import pandas as pd
# #2
# from scipy.stats import chi2_contingency
# #3
# from sklearn.model_selection import train_test_split
# from sklearn import metrics
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.tree import export_graphviz
# import pydot


#%%
import pandas as pd

data5=pd.read_csv('Dataset_05.csv')

# =============================================================================
# 1.위의 표에 표시된 데이터 타입에 맞도록 전처리를 수행하였을 때, 데이터 파일 내에
# 존재하는 결측값은 모두 몇 개인가? 숫자형 데이터와 문자열 데이터의 결측값을
# 모두 더하여 답하시오.
# (String 타입 변수의 경우 White Space(Blank)를 결측으로 처리한다) (답안 예시) 123
# =============================================================================
data5.info()

data5.isnull().sum().sum()

# 정답: 1166


#%%

# =============================================================================
# 2.이어지는 분석을 위해 결측값을 모두 삭제한다. 그리고, 성별이 세분화(Segmentation)에
# 영향을 미치는지 독립성 검정을 수행한다. 수행 결과, p-value를 반올림하여 소수점
# 넷째 자리까지 쓰고, 귀무가설을 기각하면 Y로, 기각할 수 없으면 N으로 기술하시오. 
# (답안 예시) 0.2345, N
# =============================================================================

from scipy.stats import chi2_contingency

q2=data5.dropna()
q2.columns
# ['ID', 'Age', 'Age_gr', 'Gender', 'Work_Experience', 'Family_Size',
#        'Ever_Married', 'Graduated', 'Profession', 'Spending_Score', 'Var_1',
#        'Segmentation']
q2_tab=pd.crosstab(index=q2.Gender,
                   columns=q2.Segmentation)

round(chi2_contingency(q2_tab)[1],4)

# 정답: 0.0031

#%%

# =============================================================================
# 3.Segmentation 값이 A 또는 D인 데이터만 사용하여 의사결정 나무 기법으로 분류
# 정확도를
# 측정해 본다. 
# - 결측치가 포함된 행은 제거한 후 진행하시오.
# - Train대 Test 7대3으로 데이터를 분리한다. (Seed = 123)
# - Train 데이터를 사용하여 의사결정나무 학습을 수행하고, Test 데이터로 평가를
# 수행한다.
# - 의사결정나무 학습 시, 다음과 같이 설정하시오:
# • Feature: Age_gr, Gender, Work_Experience, Family_Size, 
#             Ever_Married, Graduated, Spending_Score
# • Label : Segmentation
# • Parameter : Gini / Max Depth = 7 / Seed = 123
# 이 때 전체 정확도(Accuracy)를 소수점 셋째 자리 이하는 버리고 소수점 둘째자리까지
# 기술하시오.
# (답안 예시) 0.12
# =============================================================================

q3=q2[q2.Segmentation.isin(['A','D'])]

from sklearn.model_selection import train_test_split

train, test=train_test_split(q3,
                             test_size=0.3,
                             random_state=123)


len(q3.columns)
# Age_gr, Gender, Work_Experience, Family_Size, 
# Ever_Married, Graduated, Spending_Score
# ['ID', 'Age', 'Age_gr', 'Gender', 'Work_Experience', 'Family_Size',
#        'Ever_Married', 'Graduated', 'Profession', 'Spending_Score', 'Var_1',
#        'Segmentation']

x_var=['Age_gr', 'Gender', 'Work_Experience', 'Family_Size',
       'Ever_Married', 'Graduated','Spending_Score']


from sklearn.tree import DecisionTreeClassifier

dt=DecisionTreeClassifier(max_depth=7, random_state=123)
dt.fit(train[x_var], train.Segmentation)

acc=dt.score(test[x_var], test.Segmentation)

acc

# 정답: 0.6807116104868914 => 0.68





