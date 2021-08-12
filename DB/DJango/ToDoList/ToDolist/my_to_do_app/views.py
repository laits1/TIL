from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request) :
    return render(request,'my_to_do_app/index.html') #Templates/my_to_do_app/index.html
    # return HttpResponse("my_to_do_app first page")
    # 요청에 대한 응답객체를 생성해서 바로 클라이언트로 반환

def createTodo(request) :
    # 사용자가 메모에 입력해서 넘긴 값을 반환하는 코드
    user_input_str = request.POST['todoContent']
    return HttpResponse("입력한 메모 data는 : " + user_input_str)
    # return HttpResponse("create toDo 메모 작성 ")