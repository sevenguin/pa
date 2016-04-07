from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.
def introduce(request): 
	return JsonResponse({'code':0}) 

def setvalue(tablename, field, value, userid): 
	if userid == 0:
		table = eval(tablename)()
		setattr(table, field, value)
		table.save()
	else:
		table = eval(tablename).objects.get(userid=userid)
		setattr(table, field, value)
		table.save()