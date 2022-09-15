from django.db import models

# Create your models here.
class Article(models.Model): # 테이블 이름은  appname_class
    # primary-key ==> 정의를 안하면 기본적으로 id 라는 필드가 자동으로 생성/unique한 값(1 -> 2 -> 3 -> ..........)
    # 필드 정의 ==> 이름 = 필드타입()
    title = models.CharField(max_length=10) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}--{self.content}'