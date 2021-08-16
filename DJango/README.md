# Django 



## 1. 프로젝트 생성

1) 파이참 File -> new Project 

<img src="pic/make_project.png" style="zoom:60%;" />



2. 터미널에 장고 인스톨  및 장고 프로젝트 시작

   - pip install django
   - django-admin startproject ToDoList

   ![](pic/pip_django.png)



3. Application 구성하기

   - ToDoList 디렉터리 에서 python manage.py startapp my_to_do_app

     ![](pic/startapp.png)



4. App 구성 시 settings.py에 NSTALLED_APPS = '앱' 추가를 해야한다. 

   - ToDoList/settings.py 파일 열고 INSTALLED_APPS ='my_to_do_app' 에 앱 이름 등록

   ​	![](pic/settings1.png)



5. Django migrate 진행
   : 데이터베이스에 테이블, 필드 등의 변경이 발생했을 때 지정된 데이터베이스에 적용하는 과정을 의미

   - python manage.py migrate

     ![](pic/migrate.png)



6. 서버 구동 코드

   - python manage.py runserver

   - http://127.0.0.1:8000/

     ![](pic/runserver1.png)



7. runserver 했을 때 접속 페이지를 변경하기 위해서 urls.py 수정

   ```python
   path('admin/', admin.site.urls)
   ```

   - 코드는 사용자가 admin/ 에 접근했을 때 실제로는 http://127.0.0.1:8000/admins에 접근 했을 때 admin.site.urls로 접근하라는 의미. 
   - 우리는 사용자가 접근했을 때 기본 ToDoList 화면을 보여주려고 한다. 그 화면은 my_to_do_app 이라고 application을 만들었다.
   - 그러므로 my_to_do_app 이라는 app의 urls.py 파일로 처리를 넘겨주어야 한다. 
   - path('', include('my_to_do_app.urls')) 를 추가한다. (include 함수를 import에 추가한다.)

   ```python
   #ToDoList/ToDoList/urls.py
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('', include('my_to_do_app.urls')), # my_to_do_app.urls.py 파일을 생성해야함
       # http://127.0.0.1:8000 으로 시작하는 모든 요청은 my_to_do_app.urls 로 전달
       path('admin/', admin.site.urls), # 장고가 제공하는 관리자 사이트의 URL 완성이므로 필요하면 사용 하면 됨
       # http://127.0.0.1/admin/ : 현재 파일에서 매칭		
   ]
   
   ```

   

8. my_to_do_app폴더 밑에 urls.py 생성

   ```python
   # my_to_do_app > urls.py
   from django.urls import path
   from . import views
   urlpatterns = [
       path('', views.index, name = 'index')
   ]
   ```



9. views.py에 사용할 함수를 만들면, 그 함수를 urls.py에서 사용할 수 있다.

   - urls.py에서 특정위치로 접근한 사용자에게 어떤 화면을 보여줄지 실제로 처리하는 것이 views.py 파일

   - urls.py 파일에서 index 함수를 처리하도록 했으므로 다음과 같이 index 함수를 생성한다.

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   
   # Create your views here.
   def index(request) :
       return HttpResponse("my_to_do_app first page")
   ```

   - 여기까지 작성하고, python manage.py runserver를 실행하면, my_to_do_app first page 문구가 나오는 화면을 볼 수 있다.

   

10.  HTML 템플릿 사용

- ToDoList 페이지가 조금 꾸며진 HTML 템플릿을 사용하기 위해서 my_to_do_app 폴더 밑에 templates 폴더 만들고 , 그 안에 my_to_do_app 폴더를 만든다.
- 장고는 HTML 파일을 템플릿을 사용할 때, 해당 앱에서 ``templates`` 라는 폴더를 탐색한다.
- 그리고 동일한 앱의 이름으로 된 폴더를 찾아 그 내부에 있는 html 파일을 불러와 사용한다.
- 따라서 html 파일을 사용할 때 항상 app 내부에 templates 라는 폴더와 templates 라는 폴더 내부에 app 이름과 동일한 폴더가 존재하고, 그안에 html 파일이 존재 해야한다.
- templates 폴더에 index.html 파일 복사

 

11. index.html 을 웹 브라우저에 보여주기위한 처리는 views.py 에서한다

- html 파일을 사용자에게 보여 주려면 render 함수를 사용
- 

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return render(request,'my_to_do_app/index.html')
    # 요청에 대한 응답객체를 생성해서 바로 클라이언트로 반환

```



12. ToDoList/my_to_do_app/models.py 수정

    - models.py를 수정했으면 python manage.py makemigrations 로 서버 반영해야한다

    ```python
    from django.db import models
    
    # Create your models here.
    class Todo(models.Model) : # modles.Model 을 상속받아 Django 모델 class 생성
        # 컬럼 지정 - 기본키 생성안하면 자동 생성
        content = models.CharField(max_length=255)
    ```

python manage.py migrate



13. run server 해서 메모하기 버튼 클릭시 404 error 확인



14. ToDoList/ToDoList/urls.py 수정

    ```python
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('', include('my_to_do_app.urls')), # my_to_do_app.urls.py 파일을 생성해야함
        # http://127.0.0.1:8000 으로 시작하는 모든 요청은 my_to_do_app.urls 로 전달
        path('admin/', admin.site.urls), # 장고가 제공하는 관리자 사이트의 URL 완성이므로 필요하면 사용 하면 됨
        # http://127.0.0.1/admin/ : 현재 파일에서 매칭
    ]
    ```

    

15. ToDoList/my_to_do_app/urls.py 수정

    ```python
    # my_to_do_app > urls.py
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.index, name = 'index'),
        # root url conf에 의해서 http://127.0.0.1:8000의 요청이 전달되면
        # views.py 파일의 index 함수 코드를 실행
        # http://127.0.0.1:8000 url 별명은 'index'
    
        # http://127.0.0.1:8000/createTodo/ 요청에 대한 설정
        path('createTodo/', views.createTodo, name='createTodo')
    ]
    ```









16. ToDoList/my_to_do_app/views.py 수정

    ```python
    from django.shortcuts import render
    from django.http import HttpResponse, HttpResponseRedirect
    from .models import *
    
    # Create your views here.
    def index(request) :
        todos = Todo.objects.all() # select * from my_to_do_app_todo;
        # template으로 전달할 dict 구성
        content = {'todos':todos} # index.html에서 동적으로 코드를 생성할 때 dict를 사용
        return render(request,'my_to_do_app/index.html', content) 
    
    def createTodo(request) :
        # 사용자가 메모에 입력해서 넘긴 값을 반환하는 코드
        user_input_str = request.POST['todoContent']
        new_todo = Todo(content=user_input_str) # insert into todo(content) values (input_str)
        new_todo.save() # db에 반영
    
        return HttpResponseRedirect(reverse('index'))
        
    ```

    

17. index.html 수정

    ```html
    <div class="toDoDiv">
                    <ul class="list-group"> /* content = {'todos':todos} */
                        {% for todo in todos %}
                        <form action="" method="GET">
                            <div class="input-group" name='todo1'>
                                <li class="list-group-item">{{ todo.content }}</li>
                                <input type="hidden" id="todoNum" name="todoNum" value="1"></input>
                                <span class="input-group-addon">
                                    <button type="submit" class="custom-btn btn btn-danger">완료</button>
                                </span>
                            </div>
                        </form>
                        {% endfor %}
                    </ul>
    ```

runserver 해서 메모버튼 클릭시 추가되는지 확인



18.  메모 삭제버튼 index.html 수정

    ```html
    <form action="./doneTodo/" method="GET">
                            <div class="input-group" name='todo1'>
                                <li class="list-group-item">{{ todo.content }}</li>
                                <input type="hidden" id="todoNum" name="todoNum" value="{{todo.id}}"></input>
    ```



19. my_to_do_app/urls.py 에 path 추가

    ```python
    path('doneTodo/', views.doneTodo, name='doneTodo') # 추가
    ```



20. views.py에 함수 추가

    ```python
    def doneTodo(request) :
        # 삭제할 메모의 id 저장
        done_todo_id = request.GET['todoNum']
        print("완료한 메모의 id ", done_todo_id)
        todo = Todo.objects.get(id=done_todo_id) # 넘어온 done_todo_id와 동일한 기본키를 찾아서 해당 레코드를 반환
        todo.delete() # 반환된 객체에 대해 delete 진행
        return HttpResponseRedirect(reverse('index'))
    ```




page 138

