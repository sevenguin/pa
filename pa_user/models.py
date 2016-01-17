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
