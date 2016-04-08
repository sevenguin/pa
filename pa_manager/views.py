import logging
import traceback

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from pa.errorcode import *
from pa.question import *

logger = logging.getLogger(__name__)
# Create your views here.
def introduce(request): 
    return JsonResponse({'code':0}) 

def response(request):
    try:
        questionid = request.GET.get('questionid')
        answerinfo = request.GET.get('answer')
        userid = request.GET.get('userid')
        if not userid:
            userid = 0
        cur_question = questions['manager'][questionid]
        userid = setvalue(cur_question['answer_table'], cur_question['answer_field'], answerinfo, userid)
        next_q_base = models['manager'][questionid]
        code = 0
        nextid = 0
        next_question = questions[next_q_base['next_question_model']][next_q_base['next_question']]
        next_model = next_q_base['next_question_model']
        nextid = next_q_base['next_question']
        logger.error(next_question)
        return JsonResponse({'code': code, 'message': errcode2message[code], \
                             'data': {'questionifo': next_question['questioninfo'],
                                      'questionid': nextid,
                                      'questoinmodel': next_model,
                                      'userid': userid}})
    except Exception as e:
        code = -1
        logger.error('error info:%s' % e.args)
        traceback.print_exc()
    return JsonResponse({'code': code, 'message': errcode2message[code]})

def setvalue(tablename, field, value, userid): 
    if int(userid) == 0:
        table = eval(tablename)()
        setattr(table, field, value)
        table.save()
        userid = table.userid
    else:
        table = eval(tablename).objects.get(userid=userid)
        setattr(table, field, value)
        table.save()
    return userid