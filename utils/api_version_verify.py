#!/usr/bin/python
# -*- coding: UTF-8 -*
from functools import wraps

from flask import request

def api_version(func):
    """
    API版本验证装饰器
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # xml = request.args.get('format')
        # 验证api版本
        # verify_result, version_res = req.verify_version(kwargs.get('version'), xml)
        # if not verify_result:
        #     return version_res
        return func(*args, **kwargs)

    return wrapper