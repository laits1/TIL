from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request) :
    return render(request, 'my_to_do_app/index.html')
    # return HttpResponse("my_to_do_app first page")

def createTodo(request) :
    # 사용자가 메모에 입력해서 넘긴 값을 반환하는 코드
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str) # insert into todo(content) values (input_str)
    new_todo.save() # db에 반영

    return HttpResponse("입력한 메모 data는 : " + user_input_str)
    # return HttpResponse("create toDo 메모 작성 ")