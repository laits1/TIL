# 1000초는 몇분 몇초인가?
seconds = 1000
minutes = seconds // 60 # 몫, 분
remainder = seconds % 60 # 나머지

print("%d분 %d초" %(minutes,remainder))
