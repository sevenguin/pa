import re

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404

from .models import *
from pa.errorcode import *

# Create your views here.
def getquestion(request):
    user_id = request.GET.get('userid')  #需要记录下来，知道某个userid问了哪些问题
    question_id = request.GET.get('questionid')
    status = request.GET.get('status')
    
    modeule = get_object_or_404(t_modules, cur_questionid=int(question_id), cur_value=int(status))

    code = 0; data = []
    question = t_questions()
    try:
        question = get_object_or_404(t_questions, questionid=modeule.next_questionid)
        #print('questionid:%d' % question.questionid)
    except Http404:
        question.questionid = 0
    ret = {'code': code, 'message':'成功', 'data':{'questionid': \
           question.questionid, 'questioninfo':question.question_info}
          }
    return JsonResponse(ret)

def sendmessage(request):
    messageinfo = request.GET.get('message')
    question_id = request.GET.get('questionid')
    userid = request.GET.get('userid')

    question = t_questions()
    question = get_object_or_404(t_questions, questionid=question_id)

    user = None
    print('userid, toppicid:', userid, question.topicid, type(userid), type(question.topicid))
    if int(userid) == -1 and int(question.topicid) == 0:
        user = t_user()
        user.save()
        userid = user.userid
    message = t_messages(messageinfo=messageinfo, questionid=question_id, userid=userid)
    message.save()
    #通过question_id获得status_reg，然后通过message和status_reg来匹配获得status，再通过status和question_id获得下一个question_id
    status_reg = question.status_reg
    status = 0  #0表示无状态
    for key, value in eval(status_reg).items():
        # print('this is message')
        # print(value, messageinfo)
        if re.match(value, messageinfo):
            status = key
            break
    #print('key: %d, userid:%s' % (status, userid))
    return JsonResponse({'code': 0, 'message':'成功', 'data':{'questionid':question_id, \
                        'status': status, 'userid':userid}})




