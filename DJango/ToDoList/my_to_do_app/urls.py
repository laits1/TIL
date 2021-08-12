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