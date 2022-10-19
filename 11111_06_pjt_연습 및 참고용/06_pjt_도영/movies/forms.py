from dataclasses import field
from pyexpat import model
from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):

    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class' : "form-control",
                'placeholder': 'Title',
                'maxlength': 20,
            }
        )
    )

    description = forms.CharField(
        label = 'description',
        widget = forms.Textarea(
            attrs={
                'class' : "form-control",
                'placeholder': 'description',
            }
        )
    )

    class Meta:
        model = Movie
        # fields = '__all__'
        exclude= ('user', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude= ('user','movie' )
