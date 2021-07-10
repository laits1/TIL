#append : 파일 끝에 추가하는 기능
#파일 열기 모드 : a

f= open("Python_basic/file/test2.txt", 'a', encoding='utf-8')

append_data = "\nPython programming"
f.write(append_data)

#
f= open("Python_basic/file/test2.txt", 'r', encoding='utf-8')
print(f.read())

f.close()