from django.db import models

# Create your models here.
class t_user(models.Model):
    userid = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    createtime = models.DateTimeField(auto_now_add=True)
    lasttime = models.DateTimeField(auto_now=True)
    invitecode = models.CharField(max_length=20, unique=True)

    def paramtodict(self):
        data = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                data[key] = value
        return data

class t_userbaseinfo(models.Model):
    userid = models.AutoField(primary_key=True)
    everlived_place = models.CharField(max_length=2000)
    dietary_pref = models.CharField(max_length=2000)  #饮食偏好
    hometown = models.CharField(max_length=32)
    dietary_forbi = models.CharField(max_length=2000) #饮食禁忌
    mealtimes = models.CharField(max_length=521)  #就餐时间