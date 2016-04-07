import logging
import traceback

from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from pa.question import *
from pa.errorcode import *
import pa_manager
import pa_servant

# Create your views here.
logger = logging.getLogger(__name__)

def question(request):
    try:
        questionid = request.GET.get('questionid')
        cur_question = questions['greeting'][questionid]
        logger.error(cur_question)
        code = 0
        return JsonResponse({'code': code, 'message': errcode2message[code], \
                             'data': {'questionifo':cur_question['questioninfo']}})
    except Exception as e:
        code = -1
        logger.error('error info:%s' % e.args)
        traceback.print_exc()
    return JsonResponse({'code': code, 'message': errcode2message[code]})

def response(request):
    try:
        questionid = request.GET.get('questionid')
        cur_question = questions['greeting'][questionid]
        logger.error(cur_question)
        if __package__ == cur_question['proc_model']:
            return eval(cur_question['proc_func'])(request)
        return getattr(eval( + '.views'), cur_question['proc_func'])(request)
    except Exception as e:
        code = -1
        logger.error('error info:%s' % e.args)
        traceback.print_exc()
    return JsonResponse({'code': code, 'message': errcode2message[code]})

def welcome(request):
    try:
        questionid = request.GET.get('questionid')
        cur_question = questions['greeting'][questionid]
        next_q_base = models['greeting'][questionid]
        next_question = questions[next_q_base['next_question_model']][next_q_base['next_question']]
        logger.error(next_question)
        code = 0
        return JsonResponse({'code': code, 'message': errcode2message[code], \
                             'data': {'questionifo': next_question['questioninfo'],
                                      'questionid': next_q_base['next_question']}})
    except Exception as e:
        code = -1
        logger.error('error info:%s' % e.args)
        traceback.print_exc()
    return JsonResponse({'code': code, 'message': errcode2message[code]})