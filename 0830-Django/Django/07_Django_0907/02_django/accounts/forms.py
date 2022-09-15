from django.contrib.auth.forms import UserCreationForm, UserChangeForm # 1
# 권장사항
from django.contrib.auth import get_user_model # 2


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')