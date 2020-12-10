from django.urls import re_path
from helloworld import views

# 通过re_path方法添加URL配置项,指定访问地址和视图函数之间对应的关系
urlpatterns = [
    re_path(r'^hello-world/$', views.Hellowworld)
]