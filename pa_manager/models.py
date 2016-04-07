from django.db import models

# Create your models here.
class users(models.Model):
	userid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64)
	child_living_place = models.CharField(max_length=128)
	ever_living_place = models.CharField(max_length=128)
	food_favor = models.CharField(max_length=2000)
	food_prefer = models.CharField(max_length=2000)
	create_time = models.TimeField(auto_now=True)