from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력하세요.',
        }
    )

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('title', 'content',)
        # exclude = ('user',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        # fields = ('content', )  # 남겨둘 것 / 튜플 형식이든
        exclude = ['article', 'user', ] # 빼둘 것  /리스트 형식이든 둘다 사용가능

