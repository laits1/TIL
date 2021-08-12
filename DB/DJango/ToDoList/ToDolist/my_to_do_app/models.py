from django.db import models

# Create your models here.
class Todo(models.Model) : # modles.Model 을 상속받아 Django 모델 class 생성
    # 컬럼 지정 - 기본키 생성안하면 자동 생성
    content = models.CharField(max_length=255) # 교재 175 쪽