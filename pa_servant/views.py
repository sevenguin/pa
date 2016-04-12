import os
import urllib.parse
import logging
import urllib3

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from pa.errorcode import *
from pa.settings import *

logger = logging.getLogger(__name__)

# Create your views here.
def response(request):
    lat = request.GET.get('lat') #纬度
    lng = request.GET.get('lng')
    url = BAIDUMAP_SEARCH_BASE + '?query=%s&location=%s,%s&radius=2000&output=json&ak=%s' \
            % (urllib.parse.quote('美食'), lat, lng, BAIDU_MAP_AK)
          #这里的2000需要根据时间调整，如果懒的话就多点，否则就少点
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    if r.status == '200':
        print('success')
    else:
        print('failure')
    print(url)
    retinfo = eval(r.data.decode('utf-8'))
    print(type(retinfo))
    print(retinfo)
    code = retinfo['status']
    message = errcode2message[code]
    results = retinfo['results']
    data = {}
    for result in results:
        data[result['uid']] = result
    #根据sessionid取userid，然后传入userid，然后根据user的信息和周边数据给它推荐它想要的东西，所以接下来搞一下session
    userid = 0
    analysis(data, userid)
    return JsonResponse({'code':code, 'message':message, 'data':data})

def analysis(data, userid):
    pass