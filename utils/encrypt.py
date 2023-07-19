"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : OrderFormS
@File : encrypt.py
@Author : 18291962907
@Time : 2023/7/19 22:02
"""
import hashlib
from django.conf import settings


def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode("utf-8"))
    obj.update(data_string.encode("utf-8"))
    return obj.hexdigest()
