import numpy as np

def c_to_f(x) :
    return x * 1.8 + 32



data_C = np.array(range(0,100))
data_F = c_to_f(data_C)
print(data_F)

inp = int(input("섭씨 온도를 입력하세요 : "))
print("화씨 온도로 ", c_to_f(inp), "입니다.")

