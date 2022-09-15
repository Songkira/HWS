from django import forms # 1
from .models import Article # 2

class ArticleForm(forms.ModelForm):
    # title = forms.ChoiceField(
    #     choices =[('서울', '서울1'), ('대전', '대전1')],
    # ) # region(예시) 는 모델하고 관련없음 / # 따로 만든거

    # 필드에 대해서 정의 x
    class Meta:
        model = Article
        # fields = ('title', 'content', ) # 몇개 한정해서 불러올때
        fields = '__all__' # 필요한거 전부

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(
#         label = '내용:',
#         widget = forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#             }
#         ),
#     )