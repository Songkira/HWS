from django.shortcuts import render
import random
# Create your views here.
def index(request):
    nums = [1, 2, 3]
    context = {
        'name' : 'song ki-ra',
        'nums' : nums,
    } # 여러개 입력을 넣고 싶을때
    return render(request, 'articles/index.html', context) # 문자열로 파일 이름 쓰는것.
    # 세번째 인자로 딕셔너리{key:value} 형태로 입력

def greeting(request):

    foods = ['apple','banana', 'coconut']
    info = {
        'name':'Alice'
    }
    context = {
        'foods' : foods,
        'info': info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):

    foods = ['족발', '감자탕', '아구찜', '떡볶이']
    pick = random.choice(foods)
    context = {
        'foods':foods,
        'pick':pick,
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html',)

def catch(request):
    # throw의 name=message를 받아온거
    # throw.py에서 submit을 통해 제출된 이름은
    # dictionary 형태로 message 에 value값으로 저장되고
    # msg 는 'message'의 value 값 저장됨
    msg = request.GET.get('articles/message') 
    
    context = {
        # 'msg'는 key값, : msg는 value값
        'msg' : msg,
    }                           
    return render(request, 'articles/catch.html', context)

def hello(request, name) : #, age):
    context = {
        'name': name,
        # 'age' : age,
    }
    return render(request, 'articles/hello.html', context)










