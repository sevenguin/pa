#-*- coding:utf-8 -*-
import time
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.core.cache import cache

from .models import t_user
from pa.errorcode import *
# Create your views here.

INVITECODE_LEN = 6
VERIFYCODE_LEN = 2

def index(request):
    return JsonResponse(dict(code=0, message="hello index", data=""))

def login(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    code = 0; data = {}
    try:
        user = get_object_or_404(t_user, email=email)
        if password == user.password:
            data = user.paramtodict()
        else:
            code = ERROR_PASSWOrD_WRONG
    except Http404:
        code = ERROR_MODEL_QUERY_404
    finally:
        message = errcode2message.get(code, '错误信息不详')
    ret = {"code": code, "message":message, "data":data}
    return JsonResponse(ret)

def generate_invitecode(code_len):
    t = time.time()
    hash_t = str(hash(t))
    start = random.randint(0, len(hash_t) - code_len)
    end = start + code_len
    code_str = hash_t[start:end]
    chr_pos = sorted([random.randint(0, code_len), random.randint(0, code_len)])
    chr_ords = [random.randint(1, 52), random.randint(1, 52)]
    chrs = [chr(64 + c//27 * 33 + c % 26) for c in chr_ords]
    code = code_str[0:chr_pos[0]] + chrs[0] + code_str[chr_pos[0]:chr_pos[1]] + chrs[1] + code_str[chr_pos[1]:code_len]
    if len(code) < 10:
        print(code_str, chr_pos)
    return code

def register(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    while True:
        invitecode = generate_invitecode(INVITECODE_LEN)   #需要有个函数生成invitecode
        try:
            t_user.objects.get(invitecode=invitecode)
        except ObjectDoesNotExist:
            break
    code = 0; data = {}
    try:
        user = t_user.objects.create(email=email, password=password, nickname='', invitecode=invitecode)
        data = user.paramtodict()
        print("ret:", data)
    except IntegrityError as e:
        print('error: ', e.args)
        if e.args[0] == 1062:
            code = ERROR_WAS_REGISTED
        else:
            code = ERROR_REGISTED_WRONG
    finally:
        message = errcode2message.get(code, '错误信息不详')
    ret = {"code": code, "message":message, "data":data}
    return JsonResponse(ret)

def sendmail(request):
    #generate code
    verify_code = generate_invitecode(VERIFYCODE_LEN)
    #sendmail the verify_code
    #send_mail('test django mail', 'django mail object', 
    #    'scuwjei@foxmail.com', ['853076607@qq.com'], fail_silently=False, 
    #    auth_user='scuwei@foxmail.com', auth_password='familysh@1')
    return HttpResponse(None)

#test session and redis
def setsession(request):
    #cache.set('test_id', '3843384')
    request.session[0] = 233
    print('set id:%s, value:%s' % ('test_id', '3843384'))
    print('do here')
    return HttpResponse("None")

def checksession(request):
    #test_id = request.session['test_id']
    test_id = cache.get('test_id')
    print('test_id is: %s' % test_id)
    return HttpResponse(None)

