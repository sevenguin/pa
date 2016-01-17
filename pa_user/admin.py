from django.contrib import admin

# Register your models here.
from .models import t_user

class t_userAdmin(admin.ModelAdmin):
    #userid自增，所以不会显示， createtime、lasttime可以自动填充，所以不显示
    fields = ['nickname', 'password', 'invitecode', 'email']


admin.site.register(t_user)