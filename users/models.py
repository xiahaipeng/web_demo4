from django.db import models

# 用户模型类
class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')
    gender = models.BooleanField(default=False, verbose_name='性别')
    age = models.IntegerField(default=18, verbose_name='年龄')
    tel = models.CharField(max_length=11, null=True, verbose_name='电话')

    class Meta:
        # 指定迁移文件是,数据表的对应字段允许为null
        db_table = 'tb_user'
        # 模型类的解析说明,相当于注释的作用
        verbose_name = '用户表'
