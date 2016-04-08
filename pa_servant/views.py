import os
import urllib.parse
import logging
import urllib3

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from pa.settings import *

logger = logging.getLogger(__name__)

# Create your views here.
def response(request):
    url = BAIDUMAP_SEARCH_BASE + '?query=' + urllib.parse.quote('美食') +  '&location=39.915,116.404&' + \
          'radius=2000&output=json&ak=' + BAIDU_MAP_AK
          #这里的2000需要根据时间调整，如果懒的话就多点，否则就少点
    print(url)
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    if r.status == '200':
        print('success')
    else:
        print('failure')

    logger.error(r.data)
    
    return JsonResponse({})