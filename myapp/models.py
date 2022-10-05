from django.db import models


# Create your models here.

# username,password,email,sex
# 一个类对应数据库中的一张表
# 所有的类必须继承models.Model类
class UserInfo(models.Model):
    # 类属性对应表中的字段
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=18)
    email = models.EmailField(max_length=50)
    sex = models.CharField(max_length=10)


class Test(models.Model):
    name = models.CharField(max_length=20)