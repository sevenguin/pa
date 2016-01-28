from django.db import models

# Create your models here.

class t_questions(models.Model):
    questionid = models.AutoField(primary_key=True)
    question_info = models.CharField(max_length=2000)
    question_type = (('U', 'USER',
        'R', 'RECOMMANDER',
        'W', 'WELCOMDE'
        ))
    #models.CharField(max_length=2)