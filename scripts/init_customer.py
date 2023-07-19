"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : OrderFormS
@File : init_customer.py
@Author : 18291962907
@Time : 2023/7/19 22:12
"""
import os
import sys
import django


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取当前项目路径
sys.path.append(base_dir)   # 添加至系统环境变量


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OrderForm.settings')
django.setup()  # 仿造启动django


# 首先需要将当前项目路径添加至系统环境，然后导入以下模块才会找到模块路径，否则会报错
from Web import models
from utils.encrypt import md5

# level_object = models.Level.objects.filter(percent=99).update(percent=90)

models.Customer.objects.create(
    username="cjl",
    password=md5("234567"),
    mobile="18291962966",
    level_id=1,
    creator_id=1
)
