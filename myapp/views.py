from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse，用来生成响应信息


# 新增视图函数index
def index(request):
    return HttpResponse('index page...')


def pa(request):
    return HttpResponse('this is pa...')
