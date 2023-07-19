"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : OrderFormS
@File : init_admin.py
@Author : 18291962907
@Time : 2023/7/19 22:04
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

models.Administrator.objects.create(username="root", password=md5("123456"), mobile="18291962907")


