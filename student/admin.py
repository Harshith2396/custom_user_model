from django.contrib import admin
from django.contrib.auth import get_user_model
Myusers=get_user_model()
admin.site.register(Myusers)
# Register your models here.
