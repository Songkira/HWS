from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # 1
from .models import User # 2

# Register your models here.
admin.site.register(User, UserAdmin)