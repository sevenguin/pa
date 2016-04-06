from django.db import models

# Create your models here.

class t_questions(models.Model):
    questionid = models.AutoField(primary_key=True)
    topicid = models.IntegerField()
    question_info = models.CharField(max_length=2000)
    status_reg = models.CharField(max_length=2000)
    answer_field = models.CharField(max_length=64, verbose_name="answer to field, like username")
    #models.CharField(max_length=2)

class t_messages(models.Model):
    messageid = models.AutoField(primary_key=True)
    messageinfo = models.CharField(max_length=2000)
    questionid = models.IntegerField()
    time = models.TimeField(auto_now=True)
    userid = models.IntegerField()

#module-模型，按照question列表
#当前问题，当前值确定下一步走哪个
class t_modules(models.Model):
    cur_questionid = models.IntegerField()
    next_questionid = models.IntegerField()
    cur_value = models.CharField(max_length=200)

class t_user(models.Model):
    userid = models.AutoField(primary_key=True)
    createtime = models.TimeField(auto_now=True)