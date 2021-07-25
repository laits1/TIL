# Pandas Series, DataFrame 문법 정리



<h2>
   목차

1. [pd.Series(value,index)](#pdseriesvalueindex)
2. [시리즈명.index](#시리즈명index)
3. [시리즈명.index.name](#시리즈명indexname)
4. [시리즈명.values](#시리즈명values)
5. [value 값 접근](#value-값-접근)
6. [value 값 갱신](#value-값-갱신)
7. [value 값 추가](#value-값-추가)
8. [value 값 제거/삭제](#value-값-제거삭제)
9. [sum()](#sum)
10. [시리즈명.size](#시리즈명size)
11.  [len(시리즈명)](#len시리즈명)
12.  [시리즈명.shape](#시리즈명shape)
13. [시리즈명.unique()](#시리즈명unique)
14. [시리즈명.count()](#시리즈명count)
15. [시리즈명.mean()](#시리즈명mean)
16. [시리즈명.value_counts()](#시리즈명value_counts)



## pd.Series(value,index)



- **의미** 
  -  value와 index로 시리즈 생성
- **입력**
  - pd.Series([value1, value2, ...], index = [index1, index2, ...])
- **출력**
  - 1    10
    2    20
    3    30
    dtype: int64

```python
pd.Series([10,20,30], [1,2,3])
```



```python
1    10
2    20
3    30
dtype: int64
```



## 시리즈명.index

- **의미** 
  -   인덱스 접근
- **입력**
  -  시리즈명.index
- **출력**
  -  index(['홍길동', '이몽룡', '성춘향'])



```python
s.index
```

```python
Index(['홍길동', '이몽룡', '성춘향'], dtype='object')
```





## 시리즈명.index.name

- **의미** 
  -   시리즈의 인덱스에 이름 붙이기
- **입력**
  -  시리즈.index.name = '붙일 이름'
- **출력**
  -  이름
    홍길동	10
    이몽룡	20
    성춘향	30



```python
s.index.name = '이름'
s
```

```python
이름
홍길동    10
이몽룡    20
성춘향    30
dtype: int64
```





## 시리즈명.values

- **의미** 
  -  시리즈 value 값을 array 구조로 반환 
- **입력**
  -  시리즈명.values
- **출력**
  -  array([10,20,30])

```python
s.values
```

```
array([9904312, 3448737,  289045, 2466052], dtype=int64)
```





## value 값 접근

- **의미** 
  -   위치 인덱스 or 라벨 인덱스를 통해 value값 접근
- **입력**
  -  시리즈명[인덱스 위치 숫자] # 인덱스 타입이 정수면 위치 인덱스 사용 불가
  - 시리즈명['인덱스명']
  - 시리즈명.인덱스명
- **출력**
  -  value 값 출력

```python
s[0]
s['이몽룡']
s.서울
```



```python
96
100
9631482

```



## value 값 갱신

- **의미** 
  - 인덱스를 통한 value 값 갱신하기  
- **입력**
  -  시리즈명[index] = value
- **출력**
  -  갱신된 value 추출

```python
s
서울    9631482
부산    3393191
인천    2632035
대전    1490158

s['서울'] = 10000000

```



```python
서울	10000000
부산	3393191
인천	2632035
대전	1490158
```



## value 값 추가

- **의미** 
  - 인덱스를 통한 value 값 추가하기  
- **입력**
  -  시리즈명[index] = value
- **출력**
  -  추가된 value 추출

```python
s['대구'] = 1875000
s
```

```python
서울    10000000
부산     8630000
인천     2632035
대전     1490158
대구     1875000
```



## value 값 제거/삭제

- **의미** 
  - 인덱스를 통한 value 값 제거하기  
- **입력**
  -  del 시리즈명[index]
- **출력**
  -  시리즈 데이터 삭제

```python
del s['대전']
s
```

```python
서울    10000000
부산     8630000
인천     2632035
대구     1875000
```



## sum()

- **의미** 
  -   각 원소에 대해 조건식인 결과값이 True인 원소의 **개수** 계산
- **입력**
  -  (s0 >= 7).sum()
- **출력**
  -  시리즈 s0의 value값이 7이상인 조건에 True하는 원소의 개수

```python
s0
(s0 >= 7).sum() 
```

```python
1     0
2     1
3     2
4     3
5     4
6     5
7     6
8     7
9     8
10    9
dtype: int32

3
```



## 시리즈명.size

- **의미** 
  - NaN값 포함한 행 개수 반환  
- **입력**
  -  시리즈명.size
- **출력**
  -  행 개수 반환

```python
s1 = pd.Series([1,1,2,1,2,2,2,1,1,3,3,4,5,5,7,np.NaN])
s1
s1.size
```

```python
0     1.0
1     1.0
2     2.0
3     1.0
4     2.0
5     2.0
6     2.0
7     1.0
8     1.0
9     3.0
10    3.0
11    4.0
12    5.0
13    5.0
14    7.0
15    NaN
dtype: float64

16
```



## len(시리즈명)

- **의미** 
  -   NaN 값을 포함한 행 개수 반환
- **입력**
  - len(s1) 
- **출력**
  -  행 개수 반환

```python
s1
len(s1)
```

```python
0     1.0
1     1.0
2     2.0
3     1.0
4     2.0
5     2.0
6     2.0
7     1.0
8     1.0
9     3.0
10    3.0
11    4.0
12    5.0
13    5.0
14    7.0
15    NaN
dtype: float64
    
16
```



## 시리즈명.shape

- **의미** 
  - 튜플 형태로 (행,열) 크기 확인
- **입력**
  -  s1.shape
- **출력**
  -  (행,열)

```python
s1
s1.shape
```

```python
0     1.0
1     1.0
2     2.0
3     1.0
4     2.0
5     2.0
6     2.0
7     1.0
8     1.0
9     3.0
10    3.0
11    4.0
12    5.0
13    5.0
14    7.0
15    NaN
dtype: float64
    
(16,)
```



## 시리즈명.unique()

- **의미** 
  -   중복값을 제거한 value 값을 array 형태로 반환
- **입력**
  -  s1.unique()
- **출력**
  -  array([ 1.,  2.,  3.,  4.,  5.,  7., nan])

```python
s1
s1.unique()
```

```python
0     1.0
1     1.0
2     2.0
3     1.0
4     2.0
5     2.0
6     2.0
7     1.0
8     1.0
9     3.0
10    3.0
11    4.0
12    5.0
13    5.0
14    7.0
15    NaN
dtype: float64
    
aarray([ 1.,  2.,  3.,  4.,  5.,  7., nan])
```



## 시리즈명.count()

- **의미** 
  -   NaN 값을 제거한  행(value) 개수 
- **입력**
  -  s1.count()
- **출력**
  -  행 개수 반환

```python
s1
s1.count()
```

```python
0     1.0
1     1.0
2     2.0
3     1.0
4     2.0
5     2.0
6     2.0
7     1.0
8     1.0
9     3.0
10    3.0
11    4.0
12    5.0
13    5.0
14    7.0
15    NaN
dtype: float64
    
15
```



## 시리즈명.mean()

- **의미** 
  -   NaN 값을 제외시키고 평균값 계산
  - array.mean()은 NaN 값이 있으면 계산불가 (NaN 반환)
- **입력**
  -  시리즈명.mean()
- **출력**
  -  NaN 값을 제외한 평균값

```python
a = np.array([1,2,3,4,5,np.NaN]) # 결측치 포함
b = pd.Series(a)
b.mean()
```

```python
3.0
```



## 시리즈명.value_counts()

- **의미** 
  -   value 값들이 같은 값끼리 인덱스가 되고, 그 개수가 value값으로 세서 반환
- **입력**
  -  s1.value_counts()
- **출력**
  -  1.0    5
    2.0    4
    3.0    2
    5.0    2
    7.0    1
    4.0    1
    dtype: int64

```python
s1
s1.value_counts()
```

```python
0     1.0
1     1.0
2     2.0
3     1.0
4     2.0
5     2.0
6     2.0
7     1.0
8     1.0
9     3.0
10    3.0
11    4.0
12    5.0
13    5.0
14    7.0
15    NaN
dtype: float64
1.0    5
2.0    4
3.0    2
5.0    2
7.0    1
4.0    1
dtype: int64
```



## pd.DataFrame([리스트1],[리스트2])

- **의미** 

  -   리스트로 데이터프레임 생성

- **입력**

  -  pd.DataFrame(['a','b','c'],['a','a','g'])

- **출력**

  -  ```python
     	0	1	2
     0	a	b	c
     1	a	a	g
     ```

```python
df = pd.DataFrame([['a','b','c'],['a','a','g']])
df
```

```python
	0	1	2
0	a	b	c
1	a	a	g
```



## pd.DataFrame(딕셔너리)

- **의미** 

  -   딕셔너리로 데이터 프레임 생성

- **입력**

  -  pd.DataFrame({'A':[90,80,70],

    ​							'B':[85,98,75]},

    ​							index=[0,1,2])

- **출력**

  -  

```python
df1= pd.DataFrame({'A':[90,80,70],
                   'B':[85,98,75],
                   'C':[88,99,77],                   
                   'D':[87,89,86]},
                 index=[0,1,2])
df1
```

```python
	A	B	C	D
0	90	85	88	87
1	80	98	99	89
2	70	75	77	86
```



## pd.read_csv()

- **의미** 
  -   csv 파일 불러오기
- **입력**
  -  train_data = pd.read_csv('경로', index_col ='인덱스 사용할 column', usecols ='로딩하고 싶은 columns')
- **출력**
  -  csv 파일 출력

```python
train_data = pd.read_csv('../data/train.csv', 
                         index_col = 'PassengerId',
                        usecols=['PassengerId', 'Survived', 'Pclass', 'Name'])
train_data
```

```python

```



## df.head(n)

- **의미** 
  -   데이터 프레임의 처음 n행 만큼 출력, n생략하면 5행
- **입력**
  -  train_data.head(1)
- **출력**
  -  

```python
train_data.head(1)
```

```python

```



## df.tail(n)

- **의미** 
  -   데이터 프레임의 마지막 n행 만큼 출력, n 생략하면 5행
- **입력**
  -  train_data.tail(1)
- **출력**
  -  

```python
train_data.tail(1)
```

```python

```



## df.columns

- **의미** 
  -   데이터 프레임의 컬럼명(열 인덱스) 확인
- **입력**
  -  df3.columns
- **출력**
  -  Index(['지역', '2015', '2010', '2005', '2000', '2010-2015 증가율'], dtype='object')

```python
df3.columns
```

```python
Index(['지역', '2015', '2010', '2005', '2000', '2010-2015 증가율'], dtype='object')
```



## df.index

- **의미** 
  -   데이터 프레임의 인덱스(행 인덱스) 확인
- **입력**
  -  df3.index
- **출력**
  -  Index(['서울', '부산', '인천', '대구'], dtype='object')

```python
df3.index
```

```python
Index(['서울', '부산', '인천', '대구'], dtype='object')
```



## df.index.name

- **의미** 
  -   데이터프레임의 행 인덱스 이름 설정
- **입력**
  -  df3.index.name = '도시'
- **출력**
  -  

```python
df3.index.name = '도시'

```

```python

```



## df.values

- **의미** 
  -   데이터 프레임의 data 값 추출
- **입력**
  - df3.values
  - df3.values[0]
- **출력**
  - array 형태로 출력 

```python
df3.values # np.array 형태
df3.values[0]
```

```python
array([['수도권', 9904312, 9631482, 9762546, 9853972, 0.0283],
       ['경상권', 3448737, 3393191, 3512547, 3655437, 0.0163],
       ['수도권', 2890451, 2632035, 2517680, 2466338, 0.0982],
       ['경상권', 2466052, 2000002, 2456016, 2473990, 0.0141]], dtype=object)
array(['수도권', 9904312, 9631482, 9762546, 9853972, 0.0283], dtype=object)
```





## df.describe()

- **의미** 
  - 데이터 프레임의 기본 통계량 출력  
- **입력**
  - 
- **출력**
  - 

```python

```

```python
```





## df value값 갱신

- **의미** 
  -   인덱스 값을 통해 value 값 갱신
- **입력**
  - df[열이름(key)] = value
- **출력**
  - 갱신된 value 값

```python
df3['2010-2015 증가율']
df3['2010-2015 증가율'] * 100
```

```python
도시
서울    0.0283
부산    0.0163
인천    0.0982
대구    0.0141
Name: 2010-2015 증가율, dtype: float64
도시
서울    2.83
부산    1.63
인천    9.82
대구    1.41
Name: 2010-2015 증가율, dtype: float64
```



## df value값 추가

- **의미** 
  -   인덱스 값을 통해 value 값 추가
- **입력**
  - df[열이름(key)] = value
- **출력**
  - 새로운 열 추가

```python
df3['2005-2015 증가율'] =((df3['2015']-df3['2005'])/df3['2005'] * 100).round(2)
df3[['2005-2015 증가율']]
```

```python

특성	2005-2015 증가율
도시	
서울	1.45
부산	-1.82
인천	14.81
대구	0.41
```





## df value값 제거/삭제

- **의미** 
  -   인덱스 값 통해 value 값 제거
- **입력**
  - del df3['2010-2015 증가율']
- **출력**
  - 

```python
del df3['2010-2015 증가율']
```

```python

```





## np.random.seed(n)

- **의미** 
  -   난수 값 고정함수
- **입력**
  - np.random.seed(3)
- **출력**
  - 

```python

```

```python

```





## np.random.randint()

- **의미** 
  -   랜덤한 숫자 array로 반환
- **입력**
  - np.random.randint(n, size=m)
    - 0부터 n-1 사이의 숫자를 m개 랜덤으로 반환
- **출력**
  - 

```python
np.random.seed(3)   # 난수값을 고정하기 위해
np.random.randint(5, size=4)
```

```python
array([2, 0, 1, 3])
```





## df.count()

- **의미** 
  -   데이터 프레임의 count()는 각 열의 유효한 원소의 개수 반환(NaN은 세지 않는다.)
- **입력**
  - df1.count()
- **출력**
  - 0    4
    1    4
    2    4
    3    3
    dtype: int64

```python
df1
df1.count()
```

![](C:\Users\SDG\AppData\Roaming\Typora\typora-user-images\image-20210725120742187.png)



## 함수

- **의미** 
  -   
- **입력**
  - 
- **출력**
  - 

```python

```

```python

```





