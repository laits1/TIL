from django.urls import path, include
from main.views import index


app_name = 'insta' # front(html 파일)에서 url을 쉽게 조합하기 위해서도 사용됨

urlpatterns = [
    path('', index, name='index'),

]
