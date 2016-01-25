from django.contrib import admin

# Register your models here.
from .models import t_user, t_userbaseinfo

class t_userAdmin(admin.ModelAdmin):
    #userid自增，所以不会显示， createtime、lasttime可以自动填充，所以不显示
    fields = ['nickname', 'password', 'invitecode', 'email']

class t_userbaseinfoAdmin(admin.ModelAdmin):
    fields = ['xx']

admin.site.register(t_user)
admin.site.register(t_userbaseinfo)