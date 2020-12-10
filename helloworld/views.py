from django.shortcuts import render
from django.http import HttpResponse

# 定义一个view视图处理函数, 并给客户端返回响应体
def Hellowworld(request):
    return HttpResponse("<h>hellow world</h>")
