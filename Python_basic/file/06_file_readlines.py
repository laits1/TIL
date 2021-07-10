# 06_file_readlines.py

#readlines() 함수를 이용해서 전체 라인 읽어오기

print("---- 전체 라인 읽고 출력 -----")

f1 = open("Python_basic/file/test.txt", 'r', encoding='utf-8')
lines =f1.readlines()
print(lines)
f1.close()

print("---- 전체 라인 읽어서 1행씩 출력 ----------")
f2 = open("Python_basic/file/test.txt",'r', encoding='utf-8')
lines = f2.readlines() # 리스트로 생성

for line in lines :
    print(line, end='') # 리스트의 각 요소 출력

f2.close()

print("\n=====파일객체의 특징 :반복문에서 반복요소로 사용 가능 =========")

f3 = open("Python_basic/file/test.txt",'r',encoding='utf-8') #f3은 파일객체-반복문에 바로 반복요소로 사용 가능

for line in f3 : # f3.readline()  자동 수행 되면서
    print(line, end='') # 1행씩 읽어옴
f3.close()