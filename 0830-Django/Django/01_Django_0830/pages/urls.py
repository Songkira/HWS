from django.urls import path
from . import views # . <- 현재 폴더를 의미

# urlpatterns 없으면 오류뜸. 
# 비어있더라도 urlpatterns 존재하면 오류 안뜸. 
# articles 가 먼저 만들어져서 
app_name = 'pages'
urlpatterns = [
    path('index/', views.index, name='index',) # 등록되는 첫페이지를 보통 index로 씀.
]