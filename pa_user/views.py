#-*- coding:utf-8 -*-
import time
import random
import pdb

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, get_connection
from django.core.cache import cache
from email.mime.text import MIMEText

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
        code = ERROR_USER_QUERY_404
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
    verify_code_send = request.GET.get('verify_code')
    verify_code = request.session[email+'_verifycode']
    #print('key:', email+'_verifycode')

    code = 0; data = {}
    if verify_code != verify_code_send:
        code = ERROR_VERIFYCODE_WRONG

    while True:
        invitecode = generate_invitecode(INVITECODE_LEN)   #需要有个函数生成invitecode
        try:
            t_user.objects.get(invitecode=invitecode)
        except ObjectDoesNotExist:
            break
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

def sendverifycode(request):
    #generate code
    code = 0
    try:
        email = request.GET.get('email')
        verify_code = generate_invitecode(VERIFYCODE_LEN)
        html = """\
        <html>
          <head></head>
          <body>
            <p>Hi!<br>
               <b>%s</b><br>
               这是您的注册码，30分钟有效哦【来自PA】.
            </p>
          </body>
        </html>
        """ % verify_code
        msg = MIMEText(html, 'html')
        msg['Subject'] = "PA注册验证码"
        request.session[email+'_verifycode'] = verify_code
        #print('key:', email+'_verifycode')
        request.session.set_expiry(1800) #有效期30分钟
        #sendmail the verify_code
        send_mail(msg['Subject'], '', 
            'scuwei@foxmail.com', [email,], fail_silently=False, 
            html_message=html)
    except:
        code = ERROR_VERIFYCODE_GER_ERROR
    ret = {'code': code, 'message':errcode2message.get(code, '错误信息不详'), 'data':None}
    return HttpResponse(ret)

def setnickname(request):
    nickname = request.GET.get('nickname')
    userid = request.GET.get('userid')
    code = 0
    try:
        record = t_user.objects.filter(userid=userid).update(nickname=nickname)
    except:
        code = ERROR_UPDATE_ERROR

    ret = {'code':code, 'message':errcode2message.get(code, '错误信息不详'), 'data':None}
    return JsonResponse(ret)

def queryuserbaseinfo(request):
    pass
    code = 0
    ret = {'code':code, 'message':errcode2message.get(code, '错误信息不详'), 'data':None}
    return JsonResponse(ret)