# Django 



## 1. 프로젝트 생성

1) 파이참 File -> new Project 

<img src="pic/make_project.png" style="zoom:60%;" />



2. 터미널에 장고 인스톨  및 장고 프로젝트 시작

   - pip install django
   - django-admin startproject ToDoList

   ![](pic/pip_django.png)



3. django app 시작(필요한 만큼 생성)

   - ToDoList 디렉터리 에서 python manage.py startapp my_to_do_app

     ![](pic/startapp.png)



4. ToDoList/settings.py 파일 열고 INSTALLED_APPS ='my_to_do_app' 에 앱 이름 등록

   ​	![](pic/settings1.png)



5. Django migrate 진행
   : 데이터베이스에 테이블, 필드 등의 변경이 발생했을 때 지정된 데이터베이스에 적용하는 과정을 의미

   - python manage.py migrate

     ![](pic/migrate.png)



6. 서버 구동 코드

   - python manage.py runserver

   - http://127.0.0.1:8000/

     ![](pic/runserver1.png)



7. 