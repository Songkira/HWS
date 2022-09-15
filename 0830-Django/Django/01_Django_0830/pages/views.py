from django.shortcuts import render

# pages
# Create your views here.
# 모든 앱들의 templates 폴더를 같은 주머니로 본다
# 장고 는 앱 만들어진 순서대로 찾기 때문에 pages 의 index가 아니라 articles의 index를 출력
def index(request):

    return render(request, 'pages/index.html')