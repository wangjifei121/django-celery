from django.shortcuts import render,HttpResponse
import json

# Create your views here.


def add_handler(request):
   x = request.GET.get('x', '1')
   y = request.GET.get('y', '1')
   from .tasks import add
   add.delay(int(x), int(y))#  异步提交任务
   res = {'code':200, 'message':'ok', 'data':[{'x':x, 'y':y}]}
   return HttpResponse(json.dumps(res))