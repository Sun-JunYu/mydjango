from django.db import models

#导入时间域
from django.utils import timezone

# 基类
class Base(models.Model):
    
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now,null=True)

    class Meta:
        abstract = True

# 用户表
class User(Base):

    # 用户名
    username = models.CharField(max_length=200)

    # 密码
    password = models.CharField(max_length=200)

    # 头像
    img = models.CharField(max_length=200,null=True)

    # 用户类别 0普通用户  1超级管理员 2网站编辑
    type = models.IntegerField(default=0,null=True)

    # 手机号
    phone = models.CharField(max_length=200,null=True)

    # 个人主页
    num = models.IntegerField(default=0,null=True)

    # 声明表名
    class Meta:
        db_table = "user"