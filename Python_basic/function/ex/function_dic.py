studnets = {}
def show_info():
   name = input("이름 : ")
   year = int(input("학년 : "))
   age = int(input("나이 : "))
   phone = input("연락처 : ")
   studnets['name'] = name
   studnets['year'] = year
   studnets['age'] = age
   studnets['phone'] = phone
   
   print(studnets)

show_info()