#화씨 온도를 섭씨 온도로 변환

fTemp = 90
cTemp = (fTemp - 32) * 5 / 9 #정수연산
#cTemp 변수의 Type은?
print(type(cTemp))

print(cTemp)
print("%f" %cTemp)
print("%.3f" % cTemp)

print("화씨 온도%d를 섭씨온도로 변환하면 %.3f입니다."%(fTemp,cTemp))