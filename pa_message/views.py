from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import *
from pa.errorcode import *

# Create your views here.
def getquestion(request):
    question_id = request.GET.get('questionid')
    code = 0; data = []
    question = t_questions()
    try:
        question = get_object_or_404(t_questions, questionid=question_id)
    except Http404:
        question.questionid = 0
        question.question_info = '欢迎使用！'
    ret = {'code': code, 'message':'成功', 'data':{'question_id': \
           question.questionid, 'question_info':question.question_info}
          }
    return JsonResponse(ret)

