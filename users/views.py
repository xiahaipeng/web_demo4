from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import User

def register(request):
    if request.method == 'GET':
        #使用 register.html 模板文件,返回响应
        return render(request, 'register.html')
    else:
        # 获取表单post提交的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 注册用户信息数据的保存
        # create 方法的返回的是一个User模型对象,对应的是用户表用注册用户的数据
        user = User.objects.create(username=username, password=password)
        # return HttpResponse('注册成功')
        # 导入redirect 响应页面重定向,访问登录页面地址
        return redirect('/login/')

def login(request):
    if request.method == 'GET':
        # 获取客户端传递的 cookies 数据 username
        username = request.COOKIES.get('username', '')
        # 使用模板文件login.html, 返回登录界面
        return render(request, 'login.html', context={'username': username})
    else:
        # 登录业务逻辑
        # 获取 uesrname 和 password
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        # 进行用户名和密码校验
        try:
            # 根据 username 和 password 查询对应的数据是否存在
            # get 方法默认会利用查询到的数据创建一个对应的模型对象, 并将这个模型对象返回
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            # 如果 get 方法查询不到数据,会出现 模型类.DoesNotExist 异常
            # 用户名或密码错误
            return JsonResponse({'message': '登录失败'})
        else:
            response = JsonResponse({'massage': '登录成功'})
            # 判断是否需要记住登录用户名
            if remember == 'true':
                # 记住登录用户名, 设置cookie数据, 有效期为14天
                response.set_cookie('username', username, max_age=14 * 24 * 3600)
            return response